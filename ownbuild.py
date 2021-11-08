# Copyright Hannah von Reth <hannah.vonreth@owncloud.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

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
        self.config = self.root / ".craft.ini"
        self.shelf = self.root / ".craft.shelf"
        self.target = target

    def craft(self, command : [str], setup=False):
        args = [sys.executable, str(Craft.LOC / "craftmast/CraftMaster.py"),
                "--config", str(self.config),
                "--variables", f"Root={self.root}"
                             , "CiBuild=False"
                             , "CreateCache=False",
                "--target", self.target]
        if setup:
            args += ["--setup"]
        args += ["-c"] + [str(x) for x in command]
        print(" ".join(args))
        return subprocess.call(args) == 0


    def setup(self, update : bool):
        if not (Craft.LOC / "craftmast").exists():
            if not subprocess.call(["git", "clone", "https://invent.kde.org/packaging/craftmaster.git", str(Craft.LOC / "craftmast")]) == 0:
                exit(1)

        setup = update
        if not self.root.exists():
            setup = True
            self.root.mkdir()

        for  f in [".craft.ini", ".craft.shelf"]:
            dest = self.root / f
            if not dest.exists() or update:
                setup = True
                src = f"https://raw.githubusercontent.com/owncloud/client/{self.branch}/{f}"
                print(f"Download: {src} to {dest}")
                try:
                    urllib.request.urlretrieve(src, dest)
                except Exception as e:
                    print(e, file=sys.stderr)
                    exit(1)
        if not self.craft(["--unshelve", self.shelf], setup=setup):
            print("Failed to setup craft", file=sys.stderr)
            exit(1)



if __name__ == "__main__":
    defaultTarget = "windows-msvc2019_64-cl"
    if os.name != "nt":
        defaultTarget = "macos-64-clang"
    parser = argparse.ArgumentParser(prog="build")
    parser.add_argument("--target", action="store", default=defaultTarget, help=f"Specify a target to use, default is {defaultTarget!r}, use --target help to print available targets.")
    parser.add_argument("--branch", action="store", default="master", help="Specify the configuration of the branch to use, default is 'master'.")
    parser.add_argument("--update", action="store_true", default=False, help="Updates the cache settings for a specified branch.")
    parser.add_argument("args", nargs=argparse.REMAINDER)

    args = parser.parse_args()
    craft = Craft(args.branch, args.target)
    craft.setup(args.update)
    if args.args:
        if args.args[0] == "--":
            args.args.pop(0)
        craft.craft(args.args)
