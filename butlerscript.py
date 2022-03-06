###################################
## butlerscript_pub.py
## Author: Sean Castillo
## Version 1.0
## Purpose: Runs butler push commands to update an itch.io project's distributions with the local distributions
## of a Ren'Py project. This could be adjusted to upload anything with butler, but by default the name formatting is
## based on how Ren'Py names things.
###################################

## This program assumes that you have butler.exe in your path.
## https://itch.io/docs/butler/installing.html
##
## buildType is a string specific to how I use Ren'Py, which is to have a dev build and a public build.
## It is taken from my Ren'Py projects' options.py/config.version string.
## For example, if config.version is "1.25_Public", the buildType is parsed as "Public" because Ren'Py
## includes that word when the distributions are saved. Note that there is the '_' symbol.
## An underscore is added if the user does not write "blank" for the build type.
## file_exists is used to check whether the naming works.
##
## The directory is requested before the version number so that the user
## would look at the directory's folder to see the version number.
##
## The version number in the directory's name is used to parse out the
## project's Ren'Py name (which differs from the project's itch.io name).
## For that to work, the user inputted version number must match the
## directory's version number. This is probably the safest way to do this
## since Ren'Py project names are allowed to have numbers.

import os
from os.path import exists
from sys import platform


defaultItchName = "add-your-project-name-here"
defaultBuildType = "Public"
userName = "addYourItch.ioNameHere"

channelDict = {  # Key: itch.io channel, value: pairs of [file suffix, whether to update this channel]
    'linux': ["linux.tar.bz2", True],
    'mac': ["mac.zip", True],
    'windows': ["win.zip", True]
}

directory = None
slashType = "/"  # defaults to forward slash because Windows is the odd one out.
versionNumber = None
print("Distribution Update Via Butler Script")

itchName = input("Enter project name (as stated on itch.io URL), \
or only press ENTER to default to " + defaultItchName + ": ")

if not itchName:
    itchName = defaultItchName

print("\nEnter build type, or only press ENTER to default to " + defaultBuildType)
buildType = input("To keep it blank, type \"blank\": ")
if not buildType:
    buildType = defaultBuildType
if buildType.lower() == "blank":
    buildType = ""

versionFinder = -1
while versionFinder == -1:
    directory = input("\nPaste the directory of the distributions to upload \
(copy address as text -> paste): ")
    versionNumber = input("\nEnter version number (in x.xx format): ")
    versionFinder = directory.find(versionNumber)
    if versionFinder == -1:
        print("\nError: The directory's version number does not match \
your inputted version number.")

if platform == "linux" or platform == "linux2":
    indexOfLastSlash = directory.rfind("/")
elif platform == "darwin":
    indexOfLastSlash = directory.rfind("/")
else:
    indexOfLastSlash = directory.rfind("\\")  # Windows uses backslash.
    slashType = "\\"

renpyName = directory[indexOfLastSlash+1:versionFinder]  # This includes the '-' between name and version num.

print("\nYou have chosen to update " + itchName + " on itch.io to version " + versionNumber)
print("using local distributions of Ren'Py project: " + renpyName[:-1])  # Display renpyName without the '-'.
if buildType != "":
    print("Build type is: " + buildType)
else:
    print("No build type specified.")

updateLinux = True
updateMac = True
updateWindows = True
print("\nPress ENTER to push to all channels: (L)inux, (M)ac, and (W)indows.")
pushOption = input("You may subtract a channel update with -[channel name]: ")
pushOption = pushOption.lower()

if "-l" in pushOption:
    channelDict["linux"][1] = False
if "-m" in pushOption:
    channelDict["mac"][1] = False
if "-w" in pushOption:
    channelDict["windows"][1] = False

underscoreSelect = ""
if buildType != "":
    underscoreSelect = "_"

for channel in channelDict:
    if channelDict[channel][1] is True:
        PathAndFilename = "{A}{B}{C}{D}{E}{F}-{G}".format(A=directory, B=slashType, C=renpyName, D=versionNumber,
                                                          E=underscoreSelect, F=buildType, G=channelDict[channel][0])
        file_exists = exists(PathAndFilename)
        if file_exists:
            os.system("butler push {H} {I}/{J}:{K} --userversion {L}".format(H=PathAndFilename, I=userName,
                                                                         J=itchName, K=channel, L=versionNumber))
        else:
            print("This file has not been found: " + PathAndFilename)
os.system("pause")
