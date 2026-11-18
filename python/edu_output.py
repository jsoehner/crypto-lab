"""Color-coded educational output helper for crypto-lab tests and demos."""

from __future__ import annotations

import os
import sys

_USE_COLOR = not os.environ.get("NO_COLOR")

CYAN = "\033[1;36m" if _USE_COLOR else ""
YELLOW = "\033[1;33m" if _USE_COLOR else ""
MAGENTA = "\033[1;35m" if _USE_COLOR else ""
GREEN = "\033[1;32m" if _USE_COLOR else ""
DIM = "\033[2m" if _USE_COLOR else ""
RESET = "\033[0m" if _USE_COLOR else ""


def print_edu_case(title: str, problem: str, what: str, why: str) -> None:
    """Print an educational problem/what/why block for both non-programmers and engineers."""
    print(
        f"\n{DIM}----------------------------------------------------------------------{RESET}\n"
        f"{GREEN}▶ {title}{RESET}\n"
        f"  {MAGENTA}[PROBLEM]{RESET} {problem}\n"
        f"  {CYAN}[WHAT]{RESET}    {what}\n"
        f"  {YELLOW}[WHY]{RESET}     {why}",
        file=sys.stderr,
        flush=True,
    )
