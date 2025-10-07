#!/bin/bash
BRANCH="weekly-summary-$(date +'%Y-%m-%d')"
git checkout -b $BRANCH
git push origin $BRANCH

# GitHub CLIを使ったPR作成＆自動マージ
gh pr create --title "Weekly Summary $(date +'%Y-%m-%d')" --body "Auto-generated weekly summary" --base main
gh pr merge $(gh pr list --head $BRANCH --json number -q '.[0].number') --merge
