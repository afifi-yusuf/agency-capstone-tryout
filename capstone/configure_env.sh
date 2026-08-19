#!/usr/bin/env bash
set -euo pipefail

config_dir="${HOME}/.config/agency-capstone"
config_file="${config_dir}/env"

read -r -p "LLM base URL: " base_url
read -r -p "LLM model: " model
read -r -s -p "LLM API key: " api_key
printf '\n'

mkdir -p "${config_dir}"
chmod 700 "${config_dir}"
{
    printf 'export LLM_BASE_URL=%q\n' "${base_url}"
    printf 'export LLM_MODEL=%q\n' "${model}"
    printf 'export LLM_API_KEY=%q\n' "${api_key}"
    printf 'export AGENCY_CAPSTONE_IMAGE=%q\n' "agency-capstone:latest"
} > "${config_file}"
chmod 600 "${config_file}"

echo "Saved private environment to ${config_file}"

