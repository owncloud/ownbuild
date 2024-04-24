# About
This repository contains a helper script to mak it easier to setup a ownCloud build environment for ownCloud desktop client 2.7 and newer.


# Required dependencies
- https://community.kde.org/Craft#Setting_up_Craft
## On Windows
### Visual Studio 2022
 - Start `Visual Studio Installer`
  - Select `Modify`
  - Select `Desktop development with C++`
  - Go to `Individual Components`
  - Select `git`
  - Select `python2`
  - Select `python3`
  - Click the `Modify` button

# Get started
- `(py.exe|python3) ownbuild.py owncloud-client`

## Build a specific branch configuration
This will only affect the version of the dependencies.
- `(py.exe|python3) ownbuild.py --branch 5 -- owncloud-client`

## Build a specific client tag
- `(py.exe|python3) ownbuild.py --branch 5 -- --set revision=v5.2.1 owncloud-client`
- `(py.exe|python3) ownbuild.py --branch 5 -- owncloud-client`

## Use special craft commands
- `(py.exe|python3) ownbuild.py --branch 5 -- --package owncloud-client`
- `(py.exe|python3) ownbuild.py --branch 5 -- --run .\master\windows-cl-msvc2022-x86_64-debug\bin\owncloud.exe`


## Appendix
### Run with a specific target configuration
- `(py.exe|python3) ownbuild.py --branch 5 --target windows-cl-msvc2022-x86_64`
### Query available targets
- `(py.exe|python3) ownbuild.py --branch 5 --target help`


## On Linux

Note:
- ownbuild / craft uses cached binary packages from https://download.owncloud.com/desktop/craft/cache/ to speed up the compilation.

#### Prerequisites
 - `apt install python3 git g++ gcc`
 
### Build the client with owncloud dependencies

- `python3 ./ownbuild.py --branch master --target linux-64-gcc owncloud-client`
- When built, start the client like this: `./master/linux-64-gcc/bin/owncloud -s`

### Build the client with system dependencies

- TODO: find the relevant info e.g. docker image from kdeorg/ubuntu-1804-craft
