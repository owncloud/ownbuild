# Installation Guide for OwnCloud Client on Windows

This is an installation guide for developer to get the ownCloud Client run in release and debug version in QTCreator or Visual Studio on a Windows machine.

## Step 1: Install Visual Studio

- Required Version: Visual Studio 2022 [Visual Studio](<https://visualstudio.microsoft.com/downloads/>)
- During installation (or start Visual Studio Installer Press Change if already installed):
  - Select Desktop development with C++
  - Go to “Induvidual Components”
  - Select
    - Git
    - Python (2 and 3 if possible, otherwise only pyhton version that is present also if deprecated)
- You can close Visual Studio after installation

## Step 2: Install QT

- Download [QT](<https://www.qt.io/download-dev>)
- Required Version: QT 6.8.0
  - Check version here: [.craft.ini](<https://raw.githubusercontent.com/owncloud/client/master/.craft.ini>)  
    > line 16: QtVersion = 6.8.0
- During installation select:
  - QT/QT 6.8.0/MSCV 2022 64-bit
  - QT/QT 6.8.0/Additional Libraries/QT 5 Compatibility Module
  - QT/QT 6.8.0/Additional Libraries/QT Shader Tools
  - QT/QT 6.8.0/QT Debug Information Files
  - QT/Developer and Design Tools/cMake 3.29.3
  - QT/Developer and Design Tools/Ninja 1.12.0
  - QT Creator/QT Creator 14.0.2
  - QT Creator/CDB Debugger Support
  - QT Creator/Debugging Tools for Windows
- Install QT under C:\Qt

## Step 3: Get OwnCloud Builder

- Checkout/Download [OwnBuilder](<https://github.com/owncloud/ownbuild>)
- Choose a path where no white space is included!!
- In ownbuild.py, the default target is set to "windows-msvc2019_64-cl" (line 84). We need "windows-cl-msvc2022-x86_64"
  - Either replace targets in python file directly
  - or run the following command with additional "--target windows-cl-msvc2022-x86_64"
- Run the provided script (open terminal in ownbuild folder)
  - If target is adapted: ``` py ownbuild.py owncloud-client ```
  - If target is not adapted: ```py ownbuild.py owncloud-client --target windows-cl-msvc2022-x86_64```
- This script will download the owncloud client and all required libraries
- The owncloud client will be available in "\ownbuild\master\downloads\git\owncloud"

## Step 4: Build Craft Libraries (TODO)

- Change folder to craft: ```cd .\master\windows-cl-msvc2022-x86_64\craft\```
- run craft:
  - ```.\craftenv.ps1```
  - ```craft --compile --install --qmerge owncloud-client```

## Step 5: Open Code in IDE

### Preparation

No matter in which IDE the project is opened, cmake will get the error, that it cannot find ECM. That's because cmake does not know the folder where craft has installed the packages yet. To fix this do the following steps:

- Open the CMakeLists.txt in "\ownbuild\master\downloads\git\owncloud\owncloud-client"
- Add in line 9 the following line (with the path to you craft installation/ownbuild)
  - ```list(APPEND CMAKE_PREFIX_PATH "<path-to-ownbuild>/ownbuild/master/windows-cl-msvc2022-x86_64")```

### QT Creator

- Open QT Creator
- Click on "Open Project"
- Select CMakeLists.txt inside "\ownbuild\master\downloads\git\owncloud\owncloud-client"
- QT should automatically run cmake
- If changes in preparation have been done, cmake should run and find all needed libraries
- Click on the left on "Projects"
  - Release
    - to run the release, select under "build" under  "Edit Build-configuration" "Release"
    - if not done automatically press "run cmake" under "current configuration" below the table.
    - if finished, check id on the left side on the bottom, on the monitor icon, the "owncloud" project is selected and not one of the tests.
    - if it is the case, press run button on the bottom left and you should see the client gui
  - Debug
    - to run in debug mode, select under "build" under "Edit Build-configuration" "Release with debug information"
    - if not done automatically press "run cmake" under "current configuration" below the table.
    - if finished, check id on the left side on the bottom, on the monitor icon, the "owncloud" project is selected and not one of the tests.
    - if it is the case, press debug button on the bottom left and you should see the client gui (and run into breakpoints if set before)

### Visual Studio

- For Visual Studio, the dlls need to be made available via system path
  - Open Windows Settings and set system environmental variables
  - Add to PATH: path to \Qt\6.8.0\msvc2022_64\bin and \ownbuild\master\windows-cl-msvc2022-x86_64\bin
- For Visual Studio, you need to create a .sln
- Open cmake gui (installed with qt: \Qt\Tools\CMake_64\bin)
  - Source Code: path to owncloud-client ("\ownbuild\master\downloads\git\owncloud\owncloud-client")
  - Binaries: path to folder where files shall be generated (e.g. create new build folder inside owncloud-client)
- Press Configure
  - Select Visual Studio 2022
- Press Generate
- After generation "Open Project" is enabled and you can click it (will open project in Visual Studio)
- Right click on owncloud (in projects on the left), set it as start project
- Release
  - In the top line select "Release" and press run
- Debug
  - In the top line select "RelWithDebugInfo" and press run
