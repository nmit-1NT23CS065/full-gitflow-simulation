# Full Gitflow Simulation

A small Python Task Manager used to demonstrate a complete Gitflow-style development lifecycle: feature branches, pull requests, merges, releases, hotfixes, pre-commit hooks, and GitHub Actions CI.

## Project goals

- Build and test a small working Python application.
- Demonstrate a feature branch and pull request workflow.
- Run automated checks before commits with `pre-commit`.
- Run tests automatically with GitHub Actions.
- Prepare a release branch and tag a version.
- Simulate an urgent bug fix using a hotfix branch.
- Keep evidence of the workflow in GitHub pull requests, commits, tags, and Actions runs.

## Requirements

- Python 3.10+
- Git
- A GitHub account
- (Recommended) VS Code

## Run the app

```bash
python task_manager.py --help
python task_manager.py add "Finish SQL assignment"
python task_manager.py list
python task_manager.py complete 1
python task_manager.py list
```

Tasks are stored in `tasks.json` in the current working directory. The file is created when the first task is added and is intentionally ignored by Git.

## Run tests

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Install pre-commit hooks

```bash
python -m pip install -e ".[dev]"
pre-commit install
pre-commit run --all-files
```

The configured hooks check trailing whitespace, end-of-file newlines, YAML validity, and Python formatting/linting with Ruff. The first run may download hook environments.

## Gitflow simulation checklist

Follow `GITFLOW_GUIDE.md` in order. Use the GitHub website to open and merge pull requests. The guide includes the branch names and suggested commit messages.

- [ ] Create and push `develop`
- [ ] Create `feature/add-priority`, implement the feature, push it, and open a PR into `develop`
- [ ] Confirm GitHub Actions passes on the PR; merge it
- [ ] Create `release/1.0.0`, update release notes, merge into `main`, and tag `v1.0.0`
- [ ] Merge release changes back into `develop`
- [ ] Create `hotfix/fix-empty-title`, test the fix, and open a PR into `main`
- [ ] Merge hotfix into `main`, tag `v1.0.1`, and merge the fix back into `develop`
- [ ] Capture evidence and complete `EVIDENCE_CHECKLIST.md`

## CI workflow

`.github/workflows/ci.yml` runs on pushes and pull requests. It installs the project and development tools, runs Ruff checks, and runs the test suite.

## Suggested repository evidence

Include screenshots or links for:
1. Feature pull request and successful CI checks.
2. Release tag `v1.0.0`.
3. Hotfix pull request and successful CI checks.
4. Release tag `v1.0.1`.
5. GitHub Actions workflow runs.
6. `git branch --all` and `git tag` output (optional, if your instructor asks for terminal evidence).

## Important

This ZIP contains the project files and workflow guide. It does **not** create GitHub branches, pull requests, tags, or Actions runs automatically. You must perform the steps in the guide on your own GitHub repository so the evidence is real.


## Task Priorities

Each task supports three priority levels:

- **low** — for tasks that can wait.
- **normal** — for regular tasks (the default).
- **high** — for urgent tasks.

### Example

```bash
python task_manager.py add "Complete Gitflow simulation" --priority high
```

