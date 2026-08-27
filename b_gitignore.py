#Before we eventually put Python projects on Git/GitHub, there's something important:
# You normally should NOT upload your .venv folder.
# Why?
# Because .venv can contain thousands of files and all the installed packages. Instead, you upload:
# your Python code
# requirements.txt

#Then another computer can recreate the packages using in powershell:
# python -m pip install -r requirements.txt

#in the folder that has your code you will create a file called: .gitignore
#and in it you will write .venv/ 
#it tells git no to track this file

#to check whic files are tracked you can use: git status
#if git hasn't been initialised yet you can use in powershell: git init
#and the use git stauts

#.venv/
#    ↓
# contains installed packages

#requirements.txt
#    ↓
# records which packages the project needs

#.gitignore
#    ↓
# tells Git NOT to track .venv

#Git
#    ↓
# tracks your actual project files
