# Butler Push Script
### Version 1.0

This Python script runs butler's push commands to update an itch.io project's distributions with your local Ren'Py distributions. This could be adjusted to upload anything with butler, but by default the name formatting is based on how Ren'Py names things. Customize the channels to fit your project's needs; by default, Linux, Mac, and Windows are assumed.

## How to Use

 1. Have butler.exe in your path. [Installing butler Guide ](https://itch.io/docs/butler/installing.html) You must also have Python installed.
 2. Update the script to have your `defaultItchName`, `defaultBuildType`, and `userName`. As of version 1.0, these are on lines 34-36.
 3.  Run the script with the command `python butlerscript.py`. In windows, I open an explorer window at the script's location, use `Shift+Right Click->Open Powershell window here`, and then enter the command into the window that appears.
	 4. The values entered in step 2 will be assumed; to use them, press ENTER without typing anything. The `userName` is locked.
	 5. Copy and paste the directory of the distributions to use. On Windows, `Right Click->Copy address as text` on the directory bar works.
	 6. Enter the version number (in x.xx format). The purpose of this step is to verify the directory entered in the previous step. Simply read the previous line in the terminal. If the number is correct, copy it down.
	 7. Lastly, press ENTER to push the uploads. At this step, you have the option to subtract either of the three channel uploads with `-l`, `-m`, and `-w` for Linux, Mac, and Windows, respectively.

## License
GNU GENERAL PUBLIC LICENSE Version 3+
