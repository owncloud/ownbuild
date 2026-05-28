# agents.md -- ownBuild

## Repository Overview

Archived/legacy Python helper script for setting up a KDE Craft build environment for the ownCloud Desktop Client (2.7+). Licensed under BSD-2-Clause.

## Architecture & Key Paths

- `ownbuild.py` -- Main build script

## Development Conventions

- Single Python script
- Uses KDE Craft as the underlying build system

## Build & Test Commands

```bash
python3 ownbuild.py owncloud-client                   # Build client
python3 ownbuild.py --branch 5 -- owncloud-client     # Build specific branch
```

## Important Constraints

- Licensed under BSD-2-Clause. The OSPO target is Apache 2.0.
- Archived/legacy -- no active development expected.
- All contributions require a DCO sign-off.
- Do not introduce new **copyleft-licensed dependencies** (GPL, AGPL, LGPL, MPL) without explicit discussion in an issue first. This is especially important for repos that are migrating to or already under Apache 2.0, as copyleft dependencies would block or complicate that migration.


## OSPO Policy Constraints

### GitHub Actions
- **Only** use actions owned by `owncloud`, created by GitHub (`actions/*`), verified on the GitHub Marketplace, or verified by the ownCloud Maintainers.
- Pin all actions to their full commit SHA (not tags): `uses: actions/checkout@<SHA> # vX.Y.Z`
- Never introduce actions from unverified third parties.

### Dependency Management
- Dependabot is configured for automated dependency updates.
- Review and merge Dependabot PRs as part of regular maintenance.
- Do not introduce new dependencies without discussion in an issue first.

### Git Workflow
- **Rebase policy**: Always rebase; never create merge commits. Use `git pull --rebase` and `git rebase` before pushing.
- **Signed commits**: All commits **must** be PGP/GPG signed (`git commit -S -s`).
- **DCO sign-off**: Every commit needs a `Signed-off-by` line (`git commit -s`).
- **Conventional Commits & Squash Merge**: Use the [Conventional Commits](https://www.conventionalcommits.org/) format where the repository enforces it. Many repos use squash merge, where the PR title becomes the commit message on the default branch — apply Conventional Commits format to PR titles as well. A reusable GitHub Actions workflow enforces this.

## Context for AI Agents

This is a single-file Python utility. It wraps KDE Craft to automate building the ownCloud Desktop Client. The script handles platform detection and dependency resolution.
