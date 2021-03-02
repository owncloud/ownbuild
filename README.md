# About
This repository contains a helper script to mak it easier to setup a ownCloud build environment for ownCloud 2.7 and newer.


# Required dependencies
- Python 3.6+
- Git
## On recent Windows versions
 - winget install git
 - winget install python

# Get started
- `(py.exe|python3) build.py owncloud-client`

## Build a specific branch
- `(py.exe|python3) build.py --branch 2.7 owncloud-client`

## Use special craft commands
- `(py.exe|python3) build.py --branch 2.7 -- --package owncloud-client`
- `(py.exe|python3) build.py --branch 2.7 -- --run .\master\windows-msvc2017_64-cl-debug\bin\owncloud.exe`
