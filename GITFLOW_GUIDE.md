# Gitflow Simulation Guide

This guide is designed for a beginner. It uses a simplified Gitflow model with `main`, `develop`, feature branches, release branches, and hotfix branches. Do the steps in order. GitHub pull requests, tags, and Actions runs are the evidence that the lifecycle was actually performed.

## 0. One-time setup

1. Create a public GitHub repository named `full-gitflow-simulation`.
2. Upload the contents of this folder to the repository using **Add file → Upload files**, or use Git locally.
3. Ensure `README.md`, `task_manager.py`, `tests/`, `.pre-commit-config.yaml`, `pyproject.toml`, and `.github/workflows/ci.yml` are at the repository root.
4. Install Python 3.10+, Git, and (if working locally) VS Code.
5. Install development dependencies and hooks:

```bash
python -m pip install -e ".[dev]"
pre-commit install
pre-commit run --all-files
python -m pytest
```

The first CI run may fail if a file was uploaded in a way that changed the folder structure. Confirm the workflow file is exactly at `.github/workflows/ci.yml`.

## 1. Create `develop`

If using Git locally, open a terminal in the project folder:

```bash
git switch -c develop
git push -u origin develop
```

If `main` already has an initial commit, this creates `develop` from it. On GitHub, verify that both `main` and `develop` appear in the branch selector.

## 2. Feature lifecycle: add task priority

Create the feature branch:

```bash
git switch develop
git pull
git switch -c feature/add-priority
```

The starter app already has a priority field, so make a small meaningful improvement for the simulation: update the list output to sort high-priority tasks first, while retaining ID order within each priority. Add or update a test to prove the behavior. Commit and push:

```bash
git add .
git commit -m "feat: prioritize high-priority tasks in list output"
git push -u origin feature/add-priority
```

Open a GitHub pull request with:
- **base:** `develop`
- **compare:** `feature/add-priority`
- **title:** `feat: prioritize high-priority tasks in list output`

Wait for the **Python CI** check to pass. Review the diff, then click **Merge pull request**. Record the PR URL and take a screenshot showing the passing checks.

If you do not want to modify the application feature, you can use the already implemented priority option as the feature and simply make a small documentation improvement on this branch—but a code change plus test is stronger evidence.

## 3. Release lifecycle: `1.0.0`

Create a release branch from `develop`:

```bash
git switch develop
git pull
git switch -c release/1.0.0
```

Update the release notes in `CHANGELOG.md` (create it if needed) with version `1.0.0`, date, features, and test status. Commit and push:

```bash
git add CHANGELOG.md
git commit -m "chore: prepare release 1.0.0"
git push -u origin release/1.0.0
```

Open a pull request from `release/1.0.0` into `main`, wait for CI, review, and merge it. Then create a GitHub release:
1. Open **Releases** → **Draft a new release**.
2. Create a new tag `v1.0.0` targeting `main`.
3. Release title: `v1.0.0 — Initial Task Manager`.
4. Publish the release.

Finally merge `main` back into `develop` with a PR (base `develop`, compare `main`) so release-only changes are not lost.

## 4. Hotfix lifecycle: `1.0.1`

Create a hotfix branch from `main`:

```bash
git switch main
git pull
git switch -c hotfix/fix-empty-title
```

The current app rejects empty task titles. For a clear, testable hotfix exercise, fix a small issue discovered during release testing (for example, ensure task IDs remain unique after deleting the highest-numbered task, or improve the CLI error handling). Add a regression test. Run `python -m pytest`, commit, and push:

```bash
git add .
git commit -m "fix: correct issue found after release"
git push -u origin hotfix/fix-empty-title
```

Open a PR from `hotfix/fix-empty-title` into `main`. Wait for CI and merge. Draft a GitHub release with tag `v1.0.1` targeting `main`. Then open a PR from `main` into `develop` to carry the hotfix back to ongoing development.

**Do not claim a hotfix was completed until the PR is merged and the tag exists.** Capture screenshots of the PR, successful CI check, and release tag.

## 5. Pre-commit demonstration

After installing hooks, make a small Python change and intentionally add trailing whitespace. Try to commit. The hook should flag/fix the issue or stop the commit. Then stage the corrected file and commit again.

```bash
pre-commit run --all-files
```

Take a screenshot of the successful hook run. Do not leave deliberately broken formatting in the final repository.

## 6. GitHub Actions CI demonstration

Open the **Actions** tab in your repository. Open the latest `Python CI` run. It should show the lint, format, and test steps as successful. Open a PR as well to show CI runs on pull requests.

If CI fails:
- Open the failed run and read the first red step.
- For `ruff`, run `ruff check .` locally.
- For formatting, run `ruff format .`.
- For tests, run `python -m pytest`.
- Commit the fix and push again.

## 7. Evidence to submit

Use `EVIDENCE_CHECKLIST.md`. Include real repository links and screenshots from your own GitHub account. The guide and starter files are not proof that the Gitflow steps have been performed.
