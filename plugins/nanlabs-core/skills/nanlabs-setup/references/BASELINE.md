# Execution baseline

Cross-platform floor expected by NaNLABS agent workflows:

| Baseline | macOS | Windows | Linux |
| --- | --- | --- | --- |
| Git | Homebrew / system | winget (preferred) | native package manager |
| Python | Homebrew / uv | winget / uv | native / uv |
| Package manager | Homebrew | winget first | apt / dnf / pacman / etc. |
| AI clients | profile-dependent | profile-dependent | profile-dependent |

Concrete Windows package-manager policy may be refined by the Workstation ADR; this public skill only documents the conceptual baseline.
