#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_SKILLS_DIR="$ROOT_DIR/skills"
TARGET_SKILLS_DIR="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
DRY_RUN=0
OVERWRITE_MEMORY=0

for arg in "$@"; do
  case "$arg" in
    --dry-run)
      DRY_RUN=1
      ;;
    --overwrite-memory)
      OVERWRITE_MEMORY=1
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

if ! command -v rsync >/dev/null 2>&1; then
  echo "Missing required command: rsync" >&2
  exit 1
fi

copy_dir() {
  local src="$1"
  local dst="$2"
  if [[ ! -d "$src" ]]; then
    echo "Missing source skill directory: $src" >&2
    exit 1
  fi
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "Would sync $src -> $dst"
    rsync -ani --delete \
      --exclude 'memory.md' \
      "$src/" "$dst/"
    if [[ "$OVERWRITE_MEMORY" == "1" && -f "$src/memory.md" ]]; then
      echo "Would copy memory.md $src/memory.md -> $dst/memory.md"
    elif [[ -f "$src/memory.md" ]]; then
      echo "Would preserve existing memory.md at $dst/memory.md, or copy it if missing"
    fi
    return
  fi
  mkdir -p "$dst"
  rsync -a --delete \
    --exclude 'memory.md' \
    "$src/" "$dst/"
  if [[ "$OVERWRITE_MEMORY" == "1" && -f "$src/memory.md" ]]; then
    cp "$src/memory.md" "$dst/memory.md"
  elif [[ ! -f "$dst/memory.md" && -f "$src/memory.md" ]]; then
    cp "$src/memory.md" "$dst/memory.md"
  fi
}

if [[ ! -d "$SOURCE_SKILLS_DIR" ]]; then
  echo "Missing source skills directory: $SOURCE_SKILLS_DIR" >&2
  exit 1
fi

copy_dir "$SOURCE_SKILLS_DIR/role-review-matrix" "$TARGET_SKILLS_DIR/role-review-matrix"
copy_dir "$SOURCE_SKILLS_DIR/role-creator" "$TARGET_SKILLS_DIR/role-creator"

for role_dir in "$SOURCE_SKILLS_DIR"/roles/*; do
  [[ -d "$role_dir" ]] || continue
  role_name="$(basename "$role_dir")"
  copy_dir "$role_dir" "$TARGET_SKILLS_DIR/$role_name"
done

if [[ "$DRY_RUN" == "1" ]]; then
  echo "Dry run complete"
else
  echo "Synced Role Review Matrix skills to $TARGET_SKILLS_DIR"
fi
