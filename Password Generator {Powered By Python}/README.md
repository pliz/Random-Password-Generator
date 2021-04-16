    Random Password Generator Powered by Python

Any changes made to the password-gen.py file will not be updated in the Windows password generator executable. The Windows executable will need to be remade (install pyinstaller and run command 'pyinstaller  --onefile  password-gen.py')  for any changes made in the python file to be updated in the Windows executable.

To run Password Generator on Linux, simply run the python file. A bash script is in the works.

Do not delete Line 1 and 8, this will break the loop and the file will not run from clicking on the Windows executable. (must be run from a shell)

Ctrl + C keyboard interrupt will stop the Windows executable and python script.

The maximum password length is 74 characters, entering anything above 74 or a character as the desired password length will output an error and stop the script.

Edit line 3 quotation to customize what python asks. ex. passlen = int(input("enter desired password length  "))   -->    passlen = int(input("Enter Password Length   "))

The Windows executable file is simply for Windows machines that do not have python installed. (The Windows executable will still run with python installed, it's just so you don't have to go install python to run the generator)

The Windows executable will be immediately flagged as a trojan by Microsoft Windows Defender and 3 others. I can assure you this is a false positive. It seems like executables made with pyinstaller are flagged as viruses by some antiviruses, so please make sure the Windows executable is exempt from Windows Defender before trying to run the executable. A new Windows executable is in the works.

If you plan on only using the Windows executable, that is the only thing you need to download. In other words, there are no dependencies.

If anyone has any suggestions for any changes that should be made to the python or Windows executable file, please contact me at hbomb.github@gmail.com
