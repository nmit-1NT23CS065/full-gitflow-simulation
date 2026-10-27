# Evidence Checklist — Full Gitflow Simulation

Fill in the links after you perform each action in your own repository.

| Requirement | Evidence to collect | Link / status |
|---|---|---|
| Feature branch | Branch list showing `feature/add-priority` | |
| Pull request | PR from feature branch into `develop` | |
| Merge | Merged feature PR | |
| GitHub Actions CI | Passing checks on the feature PR | |
| Pre-commit hook | Screenshot of `pre-commit run --all-files` passing | |
| Release branch | `release/1.0.0` visible in branches or PR | |
| Release | GitHub release/tag `v1.0.0` | |
| Hotfix branch | `hotfix/fix-empty-title` visible in branches or PR | |
| Hotfix PR | PR from hotfix branch into `main` | |
| Hotfix release | GitHub release/tag `v1.0.1` | |
| Sync back | PR from `main` into `develop` after release/hotfix | |

## Reflection questions

Answer these in your own words for the report or viva:

1. Why is a feature branch safer than working directly on `main`?
2. What does a pull request allow a team to do before merging?
3. What is the difference between a release branch and a hotfix branch?
4. What does a pre-commit hook check, and when does it run?
5. What is continuous integration (CI)?
6. Why should a hotfix be merged back into `develop`?
7. What evidence proves that GitHub Actions ran successfully?
