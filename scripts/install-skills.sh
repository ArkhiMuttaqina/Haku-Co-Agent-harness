#!/usr/bin/env bash
set -euo pipefail

# Install only curated, sanitized skills into an explicitly selected Hermes home.
# Preflight all destinations before mutation; stage the complete copy first.

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
target_home="${1:-${HERMES_HOME:-}}"
if [[ -z "$target_home" ]]; then
  printf 'usage: %s /path/to/hermes-home\n' "$0" >&2
  exit 2
fi

target_home="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$target_home")"
protected_home="$(python3 -c 'import os; print(os.path.realpath(os.path.expanduser("~")))')"
if [[ "$target_home" == "/" || "$target_home" == "/home" || "$target_home" == "$protected_home" ]]; then
  printf 'refusing protected target: %s\n' "$target_home" >&2
  printf 'use an explicit profile-owned Hermes home or a temporary test home\n' >&2
  exit 2
fi

mapfile -t skill_dirs < <(find "$repo_root/skills" -mindepth 1 -maxdepth 1 -type d -print | sort)
if (( ${#skill_dirs[@]} == 0 )); then
  printf 'no curated skills found\n' >&2
  exit 1
fi

skills_dir="$target_home/skills"
for skill_dir in "${skill_dirs[@]}"; do
  name="$(basename "$skill_dir")"
  destination="$skills_dir/$name"
  if [[ -e "$destination" ]]; then
    printf 'refusing overwrite of existing skill: %s\n' "$destination" >&2
    exit 1
  fi
done

mkdir -p "$skills_dir"
stage="$skills_dir/.haku-coagent-install.$$"
if [[ -e "$stage" ]]; then
  printf 'refusing existing staging path: %s\n' "$stage" >&2
  exit 1
fi
cleanup() {
  case "$stage" in
    "$skills_dir"/.haku-coagent-install.*) rm -rf -- "$stage" ;;
    *) printf 'unsafe staging path during cleanup: %s\n' "$stage" >&2; exit 99 ;;
  esac
}
trap cleanup EXIT
mkdir "$stage"
for skill_dir in "${skill_dirs[@]}"; do
  cp -R -- "$skill_dir" "$stage/"
done

for skill_dir in "${skill_dirs[@]}"; do
  name="$(basename "$skill_dir")"
  mv -- "$stage/$name" "$skills_dir/$name"
  printf 'installed %s\n' "$skills_dir/$name"
done
rmdir "$stage"
trap - EXIT
printf 'PASS: installed %d curated skills\n' "${#skill_dirs[@]}"
