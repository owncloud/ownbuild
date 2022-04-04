# About
This repository contains a helper script to mak it easier to setup a ownCloud build environment for ownCloud 2.7 and newer.


# Required dependencies
- Python 3.6+
- Git
## On Windows
### Visual Studio 2022
 Install Visual Studio 2019 build tools and other dependencies
 - Start `Visual Studio Installer`
  - Select `Modify`
  - Select `Desktop development with C++`
  - Got to `Individual Components`
  - Search for `2019 C++ x64` and select it
  - Select `git`
  - Select `python2`
  - Select `python3`
  - Click the `Modify` button

# Get started
- `(py.exe|python3) ownbuild.py owncloud-client`

## Build a specific branch
- `(py.exe|python3) ownbuild.py --branch 2.10 owncloud-client`

## Use special craft commands
- `(py.exe|python3) ownbuild.py --branch 2.10 -- --package owncloud-client`
- `(py.exe|python3) ownbuild.py --branch 2.10 -- --run .\master\windows-msvc2017_64-cl-debug\bin\owncloud.exe`


## Appendix
### Run with a specificn target configuration
- `(py.exe|python3) ownbuild.py --branch 2.10 --target windows-msvc2019_64-cl`
### Query available targets
- `(py.exe|python3) ownbuild.py --branch 2.10 --target help`
