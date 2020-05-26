import argparse
import os
from pathlib import Path
import subprocess
import sys
import urllib.request

class Craft(object):
    LOC = Path(__file__).parent.resolve()

    def __init__(self, branch: str, target: str):
        self.branch = branch
        self.root = Craft.LOC / branch
        self.config = self.root / ".appveyor.ini"
        self.target = target

    def craft(self, command : [str]):
        args = [sys.executable, str(Craft.LOC / "craftmast/CraftMaster.py"),
                "--config", str(self.config),
                "--variables", f"Root={self.root}", "CiBuild=False", "--target", self.target, "-c"] + command
        print(" ".join(args))
        return subprocess.call(args) == 0


    def setup(self):
        if not (Craft.LOC / "craftmast").exists():
            if not subprocess.call(["git", "clone", "git@github.com:KDE/craftmaster.git", str(Craft.LOC / "craftmast")]) == 0:
                exit(1)

        if not self.root.exists():
            self.root.mkdir()
            src = f"https://raw.githubusercontent.com/owncloud/client/{self.branch}/.appveyor.ini"
            print(f"Download: {src}")
            urllib.request.urlretrieve(src, self.config)

            if not (self.craft(["--add-blueprint-repository", "[git]https://github.com/owncloud/craft-blueprints-owncloud.git"]) and
                    self.craft(["craft"])):
                print("Failed to setup craft", file=sys.stderr)
                exit(1)


if __name__ == "__main__":
    defaultTarget = "windows-msvc2017_64-cl"
    if os.name != "nt":
        defaultTarget = "macos-64-clang"
    parser = argparse.ArgumentParser(prog="build")
    parser.add_argument("--target", action="store", default=defaultTarget)
    parser.add_argument("--branch", action="store", default="master")
    parser.add_argument("args", nargs=argparse.REMAINDER)

    args = parser.parse_args()
    craft = Craft(args.branch, args.target)
    craft.setup()
    if args.args:
        if args.args[0] == "--":
            args.args.pop(0)
        craft.craft(args.args)
