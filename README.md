this is not a working implementation, simply a proof of concept of how it could be implemented

this was tested using the version of modengine2 shared by Amfales on the Sekiro channel in the Archipelo After Dark discord

### building it locally
- clone the repository
- run `git submodule update --init --recursive` to download the submodules
- go to the client folder
- open the project in visual studio
- make sure you have vcpkg, it should be installed together with Visual Studio, and then run `vcpkg integrate install`
- set the platform to x64 and the mode to Release and build it
