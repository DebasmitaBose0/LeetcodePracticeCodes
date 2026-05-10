#!/usr/bin/env sh
# Simple helper: show diff, prompt for commit message, commit and push
echo "Repository: $(pwd)"
echo
git status --short --branch

echo
echo "Unstaged changes (name-only):"
git diff --name-only

echo
echo "Full diff (HEAD vs working tree):"
git --no-pager diff

echo
printf "Enter commit message (leave empty to abort): "
read msg
if [ -z "$msg" ]; then
  echo "No commit message provided — aborting."
  exit 1
fi

git add -A
git commit -m "$msg"
branch=$(git rev-parse --abbrev-ref HEAD)
git push origin "$branch"

echo "Done."
