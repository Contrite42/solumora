#!/usr/bin/env python3
"""
Git Auto-Push Script

Automatically commits and pushes changes to the repository after significant
content expansions, navigation rebuilds, or component updates.

Usage:
    python git_auto_push.py [message]
    python git_auto_push.py --check  # Check for changes without committing
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def run_git_command(args, check=True, capture_output=True):
    """Run a git command and return the result."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=REPO_ROOT,
            capture_output=capture_output,
            text=True,
            check=check
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(args)}")
        print(f"Error: {e.stderr}")
        return None


def check_git_status():
    """Check if there are uncommitted changes."""
    result = run_git_command(["status", "--porcelain"])
    if result is None:
        return False, []
    
    changes = result.stdout.strip().split("\n") if result.stdout.strip() else []
    return bool(changes), changes


def get_current_branch():
    """Get the current git branch name."""
    result = run_git_command(["rev-parse", "--abbrev-ref", "HEAD"])
    if result is None:
        return None
    return result.stdout.strip()


def stage_all_changes():
    """Stage all changes in the repository."""
    print("Staging all changes...")
    result = run_git_command(["add", "-A"])
    return result is not None


def commit_changes(message):
    """Commit staged changes with the given message."""
    print(f"Committing with message: {message}")
    result = run_git_command(["commit", "-m", message])
    return result is not None


def push_changes(branch="main"):
    """Push commits to the remote repository."""
    print(f"Pushing to {branch}...")
    result = run_git_command(["push", "origin", branch], capture_output=False)
    return result is not None


def auto_commit_and_push(commit_message=None):
    """
    Automatically commit and push changes if any exist.
    
    Args:
        commit_message: Custom commit message. If None, generates a timestamp-based message.
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Check for changes
    has_changes, changes = check_git_status()
    
    if not has_changes:
        print("No changes to commit.")
        return True
    
    print(f"Found {len(changes)} changed files:")
    for change in changes[:10]:  # Show first 10
        print(f"  {change}")
    if len(changes) > 10:
        print(f"  ... and {len(changes) - 10} more")
    
    # Get current branch
    branch = get_current_branch()
    if branch is None:
        print("Error: Could not determine current branch")
        return False
    
    print(f"Current branch: {branch}")
    
    # Generate commit message if not provided
    if commit_message is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-commit: {timestamp}"
    
    # Stage, commit, and push
    if not stage_all_changes():
        print("Error: Failed to stage changes")
        return False
    
    if not commit_changes(commit_message):
        print("Error: Failed to commit changes")
        return False
    
    if not push_changes(branch):
        print("Error: Failed to push changes")
        return False
    
    print(f"\n✓ Successfully committed and pushed to {branch}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Automatically commit and push changes to git repository"
    )
    parser.add_argument(
        "message",
        nargs="?",
        help="Commit message (default: auto-generated timestamp)"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for changes without committing"
    )
    
    args = parser.parse_args()
    
    if args.check:
        has_changes, changes = check_git_status()
        if has_changes:
            print(f"Found {len(changes)} uncommitted changes")
            sys.exit(1)
        else:
            print("No uncommitted changes")
            sys.exit(0)
    
    success = auto_commit_and_push(args.message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
