from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent

old_dir = ROOT / "github" / "workflows"
new_dir = ROOT / ".github" / "workflows"

def safe_move(src: Path, dst: Path):
    if dst.exists():
        # don't overwrite: create a migrated name
        dst = dst.with_name(dst.stem + "_migrated" + dst.suffix)
    shutil.move(str(src), str(dst))
    print(f"Moved: {src} -> {dst}")

def main():
    if not old_dir.exists():
        print(f"No old workflow folder found at: {old_dir}")
        print("Nothing to do.")
        return

    new_dir.mkdir(parents=True, exist_ok=True)

    moved_any = False
    for f in old_dir.iterdir():
        if f.is_file() and f.suffix.lower() in [".yml", ".yaml"]:
            safe_move(f, new_dir / f.name)
            moved_any = True

    if not moved_any:
        print(f"No .yml/.yaml files found in: {old_dir}")

    # Optional: remove old folder if empty
    try:
        if old_dir.exists() and not any(old_dir.iterdir()):
            old_dir.rmdir()
            # remove parent github/ if empty
            parent = old_dir.parent
            if parent.exists() and not any(parent.iterdir()):
                parent.rmdir()
            print("Cleaned empty old folders.")
    except Exception:
        pass

    print("\nDone. Your workflows must live in .github/workflows for GitHub Actions to run.")

if __name__ == "__main__":
    main()