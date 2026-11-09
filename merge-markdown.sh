#!/usr/bin/env bash
#
# merge-markdown.sh - Collect all Markdown files under a directory tree into one folder.
#
# Skips common VCS, dependency, build, cache, and IDE directories by default.
# Safe to copy anywhere; no project-specific paths.
#
# Usage:
#   merge-markdown.sh -o OUTPUT_DIR [-s SOURCE_DIR] [options]
#
# Examples:
#   merge-markdown.sh -o ./all-md -s ~/Projects/myapp
#   merge-markdown.sh -o /tmp/md-export --keep-tree
#   merge-markdown.sh -o ./out --dry-run -s .
#

set -euo pipefail

VERSION="1.0.0"

# Directory names (or globs for find -name) pruned anywhere in the tree.
DEFAULT_BANNED_DIRS=(
  # Version control
  .git .svn .hg .bzr .jj

  # Dependencies / package managers
  node_modules bower_components .pnpm-store .yarn .pnp
  vendor bundles .bundle
  Pods Carthage

  # Python
  __pycache__ .venv venv .tox .nox
  .pytest_cache .mypy_cache .ruff_cache .hypothesis
  .eggs '*.egg-info' site-packages pip-wheel-metadata

  # Ruby / Java / Rust / .NET / Go artifacts
  .gradle .m2 target
  bin obj packages

  # Build / dist / frameworks
  dist build out _build
  .next .nuxt .output .svelte-kit .angular
  .turbo .parcel-cache .webpack

  # Caches and temp
  .cache cache tmp temp temporary
  coverage htmlcov .nyc_output
  .sass-cache .eslintcache .stylelintcache

  # IDE / editor / tooling (often huge or non-content)
  .idea .vscode .vs .fleet

  # OS / junk
  .Trash __MACOSX
  lost+found

  # Virtualization / infra
  .terraform .vagrant
)

SOURCE_DIR="."
OUTPUT_DIR=""
KEEP_TREE=0
DRY_RUN=0
QUIET=0
FORCE=0
USE_DEFAULT_BANS=1
EXTRA_BANS=()
BAN_ONLY=()
EXTENSIONS=("md" "markdown" "mdown" "mkd")

usage() {
  cat <<'EOF'
merge-markdown.sh - Collect Markdown files from a tree into one output folder.

Usage:
  merge-markdown.sh -o OUTPUT_DIR [-s SOURCE_DIR] [options]

Options:
  -s, --source DIR       Root directory to scan (default: current directory)
  -o, --output DIR       Destination folder (required)
  -k, --keep-tree        Preserve relative paths under OUTPUT (default: flatten)
  -n, --dry-run          List actions without copying
  -q, --quiet            Less logging
  -f, --force            Overwrite existing files in output
  --ban NAME             Extra directory name or glob to skip (repeatable)
  --ban-only NAME        Use only these banned names (disables default list)
  --no-default-bans      Do not apply built-in banned directory list
  --ext EXT              File extension without dot (repeatable; default: md, markdown, ...)
  -h, --help             Show this help
  -V, --version          Print version

Flatten mode names files as: path__to__file.md (relative to source).
EOF
}

log() {
  [[ "$QUIET" -eq 1 ]] && return 0
  printf '%s\n' "$*"
}

die() {
  printf 'merge-markdown.sh: %s\n' "$*" >&2
  exit 1
}

normalize_path() {
  local p="$1"
  if [[ -d "$p" ]]; then
    (cd "$p" && pwd -P)
    return
  fi
  local parent base
  base="$(basename "$p")"
  parent="$(dirname "$p")"
  if [[ -d "$parent" ]]; then
    printf '%s/%s\n' "$(cd "$parent" && pwd -P)" "$base"
  else
    printf '%s\n' "$p"
  fi
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      -s|--source)
        [[ $# -ge 2 ]] || die "missing value for $1"
        SOURCE_DIR="$2"
        shift 2
        ;;
      -o|--output)
        [[ $# -ge 2 ]] || die "missing value for $1"
        OUTPUT_DIR="$2"
        shift 2
        ;;
      -k|--keep-tree)
        KEEP_TREE=1
        shift
        ;;
      -n|--dry-run)
        DRY_RUN=1
        shift
        ;;
      -q|--quiet)
        QUIET=1
        shift
        ;;
      -f|--force)
        FORCE=1
        shift
        ;;
      --ban)
        [[ $# -ge 2 ]] || die "missing value for --ban"
        EXTRA_BANS+=("$2")
        shift 2
        ;;
      --ban-only)
        [[ $# -ge 2 ]] || die "missing value for --ban-only"
        BAN_ONLY+=("$2")
        shift 2
        ;;
      --no-default-bans)
        USE_DEFAULT_BANS=0
        shift
        ;;
      --ext)
        [[ $# -ge 2 ]] || die "missing value for --ext"
        EXTENSIONS+=("$2")
        shift 2
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      -V|--version)
        printf 'merge-markdown.sh %s\n' "$VERSION"
        exit 0
        ;;
      --)
        shift
        break
        ;;
      -*)
        die "unknown option: $1 (try --help)"
        ;;
      *)
        if [[ -z "$OUTPUT_DIR" ]]; then
          OUTPUT_DIR="$1"
        elif [[ "$SOURCE_DIR" == "." ]]; then
          SOURCE_DIR="$1"
        else
          die "unexpected argument: $1"
        fi
        shift
        ;;
    esac
  done
}

collect_banned() {
  local -n _out=$1
  _out=()
  if [[ ${#BAN_ONLY[@]} -gt 0 ]]; then
    _out=("${BAN_ONLY[@]}")
  else
    if [[ "$USE_DEFAULT_BANS" -eq 1 ]]; then
      _out=("${DEFAULT_BANNED_DIRS[@]}")
    fi
    if [[ ${#EXTRA_BANS[@]} -gt 0 ]]; then
      _out+=("${EXTRA_BANS[@]}")
    fi
  fi
  local out_base
  out_base="$(basename "$OUTPUT_DIR")"
  _out+=("$out_base")
}

build_prune_parts() {
  local -n _banned=$1
  local -n _parts=$2
  _parts=()
  local b
  for b in "${_banned[@]}"; do
    if [[ ${#_parts[@]} -gt 0 ]]; then
      _parts+=( -o )
    fi
    _parts+=( -name "$b" )
  done
}

build_type_parts() {
  local -n _parts=$1
  _parts=()
  local ext first=1
  for ext in "${EXTENSIONS[@]}"; do
    ext="${ext#.}"
    if [[ $first -eq 1 ]]; then
      _parts+=( \( -iname "*.${ext}" )
      first=0
    else
      _parts+=( -o -iname "*.${ext}" )
    fi
  done
  _parts+=( \) )
}

flatten_name() {
  local rel="$1"
  local base dir_part flat
  base="$(basename "$rel")"
  dir_part="${rel%/*}"
  if [[ "$dir_part" == "$rel" ]]; then
    printf '%s\n' "$base"
    return
  fi
  flat="${dir_part//\//__}__${base}"
  printf '%s\n' "$flat"
}

copy_or_plan() {
  local src="$1"
  local dest="$2"
  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "[dry-run] $src -> $dest"
    return 0
  fi
  mkdir -p "$(dirname "$dest")"
  if [[ -e "$dest" ]] && [[ "$FORCE" -eq 0 ]]; then
    log "skip (exists): $dest"
    return 0
  fi
  cp -f -- "$src" "$dest"
  log "$dest"
}

process_files() {
  local src_abs="$1"
  local out_abs="$2"
  shift 2
  local -a find_rest=( "$@" )
  local count=0 file rel dest

  while IFS= read -r -d '' file; do
    rel="${file#"$src_abs"/}"
    rel="${rel#/}"
    if [[ "$KEEP_TREE" -eq 1 ]]; then
      dest="$out_abs/$rel"
    else
      dest="$out_abs/$(flatten_name "$rel")"
    fi
    copy_or_plan "$file" "$dest"
    count=$((count + 1))
  done < <(find "$src_abs" "${find_rest[@]}")

  log "Done. ${count} markdown file(s) processed."
}

main() {
  parse_args "$@"

  [[ -n "$OUTPUT_DIR" ]] || die "output directory required (-o OUTPUT)"
  [[ -d "$SOURCE_DIR" ]] || die "source is not a directory: $SOURCE_DIR"

  local src_abs out_abs
  src_abs="$(normalize_path "$SOURCE_DIR")"
  out_abs="$(normalize_path "$OUTPUT_DIR")"

  if [[ "$out_abs" == "$src_abs" ]]; then
    die "output directory must not be the same as source directory"
  fi

  if [[ "$DRY_RUN" -eq 0 ]]; then
    mkdir -p "$out_abs"
  fi

  local -a banned=()
  collect_banned banned

  local -a prune_parts=()
  build_prune_parts banned prune_parts

  local -a type_parts=()
  build_type_parts type_parts

  if [[ ${#prune_parts[@]} -gt 0 ]]; then
    process_files "$src_abs" "$out_abs" \
      \( "${prune_parts[@]}" \) -prune -o \
      -type f "${type_parts[@]}" -print0
  else
    process_files "$src_abs" "$out_abs" \
      -type f "${type_parts[@]}" -print0
  fi
}

main "$@"
