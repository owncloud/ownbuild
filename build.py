import os
from pathlib import Path
import subprocess
import sys

LOC = Path(__file__).parent.resolve()

def craft(args : [str]):
    args = [sys.executable, str(LOC / "craftmast/CraftMaster.py"),
            "--config", str(LOC / ".appveyor.ini"),
            "--target", "windows-msvc2017_64-cl",
            "--variables", f"Root={LOC}", "CiBuild=False",
            "-c"] + args
    print(" ".join(args))
    return subprocess.call(args) == 0

if not (LOC / "craftmast").exists():
    if not (subprocess.call(["git", "clone", "git@github.com:KDE/craftmaster.git", str(LOC / "craftmast")]) == 0 and
            craft(["--add-blueprint-repository", "[git]https://github.com/owncloud/craft-blueprints-owncloud.git"]) and
            craft(["craft"])):
        print("Failed to setup craft", file=sys.stderr)
        exit(1)

craft(sys.argv[1:])
