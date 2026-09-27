#!/usr/bin/env bash
set -euo pipefail

source_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
destination="$HOME/Videos/florence"

mkdir -p "$destination/assets"
cp -- "$source_dir/index.html" "$source_dir/style.css" "$destination/"
cp -R -- "$source_dir/assets/." "$destination/assets/"

printf 'Copied the web page to %s\n' "$destination"
