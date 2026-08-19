import json
import os

import pytest

from capstone.mini_swe import (
    RepairTask,
    load_manifest,
    load_private_environment,
    prepare_workspace,
    run_test,
)
from capstone.run_benchmark import aggregate_results, batches


def test_manifest_is_pinned_and_tasks_are_unique():
    revision, tasks = load_manifest()

    assert len(revision) == 40
    assert len(tasks) >= 6
    assert len({task.name for task in tasks}) == len(tasks)


def test_manifest_rejects_unsafe_paths(tmp_path):
    manifest = tmp_path / "tasks.json"
    manifest.write_text(
        json.dumps(
            {
                "revision": "a" * 40,
                "tasks": [
                    {
                        "name": "escape",
                        "program": "../answer.py",
                        "test": "test_answer.py",
                        "category": "invalid",
                    }
                ],
            }
        )
    )

    with pytest.raises(ValueError, match="unsafe path"):
        load_manifest(manifest)


def test_private_environment_restores_profiled_process_settings(tmp_path, monkeypatch):
    env_file = tmp_path / "env"
    env_file.write_text(
        "export LLM_BASE_URL=http://example.test:18000/v1\n"
        "export LLM_MODEL=example/model\n"
        "export LLM_API_KEY=private-value\n"
    )
    for key in ("LLM_BASE_URL", "LLM_MODEL", "LLM_API_KEY"):
        monkeypatch.delenv(key, raising=False)

    assert load_private_environment(env_file) is True
    assert os.environ["LLM_BASE_URL"] == "http://example.test:18000/v1"
    assert os.environ["LLM_API_KEY"] == "private-value"


def test_prepare_workspace_removes_reference_implementations(tmp_path):
    source = tmp_path / "source"
    (source / "python_programs").mkdir(parents=True)
    (source / "python_testcases").mkdir()
    (source / "correct_python_programs").mkdir()
    (source / "java_programs").mkdir()
    (source / ".git").mkdir()
    (source / "python_programs" / "gcd.py").write_text("def gcd(a, b): return a\n")
    (source / "python_testcases" / "test_gcd.py").write_text("def test_gcd(): pass\n")
    (source / "correct_python_programs" / "gcd.py").write_text("secret\n")

    task = RepairTask("gcd", "python_programs/gcd.py", "python_testcases/test_gcd.py", "math")
    destination = prepare_workspace(source, tmp_path / "workspace", task)

    assert (destination / task.program).is_file()
    assert not (destination / "correct_python_programs").exists()
    assert not (destination / "java_programs").exists()
    assert not (destination / ".git").exists()


def test_run_test_reports_success_and_failure(tmp_path):
    tests = tmp_path / "python_testcases"
    programs = tmp_path / "python_programs"
    tests.mkdir()
    programs.mkdir()
    test_file = tests / "test_sample.py"
    test_file.write_text("def test_sample():\n    assert True\n")
    (programs / "sample.py").write_text("VALUE = 1\n")
    task = RepairTask(
        "sample", "python_programs/sample.py", "python_testcases/test_sample.py", "fixture"
    )

    assert run_test(tmp_path, task)["passed"] is True
    test_file.write_text("def test_sample():\n    assert False\n")
    result = run_test(tmp_path, task)
    assert result["passed"] is False
    assert result["returncode"] == 1


def test_batches_and_aggregate_results():
    assert batches([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    with pytest.raises(ValueError):
        batches([1], 0)

    summary = aggregate_results(
        [
            {"success": True, "duration_s": 1.0},
            {"success": False, "duration_s": 3.0},
        ],
        mode="parallel",
        parallelism=2,
    )
    assert summary["repair_rate"] == 0.5
    assert summary["task_duration_mean_s"] == 2.0
