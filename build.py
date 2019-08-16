import os
from pathlib import Path
import subprocess
import sys

LOC = Path(__file__).parent.resolve()

def craft(command : [str]):
    args = [sys.executable, str(LOC / "craftmast/CraftMaster.py"),
            "--config", str(LOC / ".appveyor.ini"),
            "--variables", f"Root={LOC}", "CiBuild=False"]
    if os.name == "nt":
        args += ["--target", "windows-msvc2017_64-cl"]
    args += ["-c"] + command
    print(" ".join(args))
    return subprocess.call(args) == 0

if not (LOC / "craftmast").exists():
    if not (subprocess.call(["git", "clone", "git@github.com:KDE/craftmaster.git", str(LOC / "craftmast")]) == 0 and
            craft(["--add-blueprint-repository", "[git]https://github.com/owncloud/craft-blueprints-owncloud.git"]) and
            craft(["craft"])):
        print("Failed to setup craft", file=sys.stderr)
        exit(1)

craft(sys.argv[1:])
