# ownBuild

<!-- OSPO-managed README | Generated: 2026-04-16 | v2 -->

[![License](https://img.shields.io/badge/License-BSD--2--Clause-blue.svg)](LICENSE) [![ownCloud OSPO](https://img.shields.io/badge/OSPO-ownCloud-blue)](https://kiteworks.com/opensource)

A Python helper script that simplifies setting up a KDE Craft-based build environment for the ownCloud Desktop Client (version 2.7+). It automates dependency resolution and compilation across Windows, Linux, and macOS using the Craft package manager.

> **Note:** This repository is in maintenance/legacy mode and is no longer actively developed.

## Getting Started

Follow the steps below to set up the build environment.

### Prerequisites

- Python 3
- [KDE Craft](https://community.kde.org/Craft#Setting_up_Craft)
- On Windows: Visual Studio 2022 with C++ workload, Git, Python 2/3
- On Linux: `python3 git g++ gcc`

### Build the Desktop Client

```bash
python3 ownbuild.py owncloud-client
```

### Build a Specific Branch

```bash
python3 ownbuild.py --branch 5 -- owncloud-client
```

### Build a Specific Tag

```bash
python3 ownbuild.py --branch 5 -- --set revision=v5.2.1 owncloud-client
```

## Documentation

- [KDE Craft Documentation](https://community.kde.org/Craft)
- [ownCloud Desktop Client](https://github.com/owncloud/client)

## Part of ownCloud Infrastructure

This tool supports building the [ownCloud Desktop Client](https://github.com/owncloud/client) from source.

> **Note:** This repository is archived/legacy.

## Community & Support

**[Star](https://github.com/owncloud/ownbuild)** this repo and **Watch** for release notifications!

- [ownCloud Website](https://owncloud.com)
- [Community Discussions](https://github.com/orgs/owncloud/discussions)
- [Matrix Chat](https://app.element.io/#/room/#owncloud:matrix.org)
- [Documentation](https://doc.owncloud.com)
- [Enterprise Support](https://owncloud.com/contact-us/)
- [OSPO Home](https://kiteworks.com/opensource)

## Contributing

We welcome contributions! Please read the [Contributing Guidelines](CONTRIBUTING.md)
and our [Code of Conduct](CODE_OF_CONDUCT.md) before getting started.

### Workflow

- **Rebase Early, Rebase Often!** We use a rebase workflow. Always rebase on the target branch before submitting a PR.
- **Dependabot**: Automated dependency updates are managed via Dependabot. Review and merge dependency PRs promptly.
- **Signed Commits**: All commits **must** be PGP/GPG signed. See [GitHub's signing guide](https://docs.github.com/en/authentication/managing-commit-signature-verification).
- **DCO Sign-off**: Every commit must carry a `Signed-off-by` line:
  ```
  git commit -s -S -m "your commit message"
  ```
- **GitHub Actions Policy**: Workflows may only use actions that are (a) owned by `owncloud`, (b) created by GitHub (`actions/*`), or (c) verified in the GitHub Marketplace.

## Security

**Do not open a public GitHub issue for security vulnerabilities.**

Report vulnerabilities at **<https://security.owncloud.com>** -- see [SECURITY.md](SECURITY.md).

Bug bounty: [YesWeHack ownCloud Program](https://yeswehack.com/programs/owncloud-bug-bounty-program)

## License

This project is licensed under the [BSD-2-Clause](LICENSE).

## About the ownCloud OSPO

The [Kiteworks Open Source Program Office](https://kiteworks.com/opensource), operating under
the [ownCloud](https://owncloud.com) brand, launched on May 5, 2026, to steward the open source
ecosystem around ownCloud's products. The OSPO ensures transparent governance, license compliance,
community health, and sustainable collaboration between the open source community and
[Kiteworks](https://www.kiteworks.com), which acquired ownCloud in 2023.

- **OSPO Home**: <https://kiteworks.com/opensource>
- **GitHub**: <https://github.com/owncloud>
- **ownCloud**: <https://owncloud.com>

For questions about the OSPO or licensing, contact ospo@kiteworks.com.

### License Migration to Apache 2.0

The OSPO is driving a strategic relicensing of ownCloud repositories toward the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), following
the [Apache Software Foundation's third-party license policy](https://www.apache.org/legal/resolved.html).

Individual repositories will migrate as their audit is completed. The LICENSE file
in each repo reflects its **current** license status (not the target).

**Current license: BSD-2-Clause** (Category A per Apache policy -- permissive, compatible with Apache-2.0).

Migration prerequisites for this repository:

- **CLA/DCO coverage**: All past contributors must have signed agreements permitting relicensing
- **Header updates**: All source file headers must be updated to Apache-2.0 notice
- **Dependency audit**: Verify no incompatible transitive dependencies
