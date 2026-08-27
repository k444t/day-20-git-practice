#.venv forms a virtual environment 
#imagine if you have multiple projects
#If everything is installed into the same global Python installation, packages from completely unrelated projects start getting mixed together.
# And eventually you might have an even worse problem:
# Project A needs:
# package version 2
# Project B needs:
# package version 3
#Think of venv as a private Python box
# Without a virtual environment:
# Your computer's Python
# │
# ├── requests
# ├── selenium
# ├── openai
# ├── pandas
# ├── numpy
# └── EVERYTHING 😭

#With virtual environments:
# Weather Project
# └── .venv
#     └── requests

#AI Project
# └── .venv
#     ├── openai
#     └── requests

#Data Project
# └── .venv
#     ├── pandas
#     └── numpy

#Each project gets its own packages.
# And importantly, venv does not mean you're installing an entirely different Python programming language.
# It's an isolated environment based on your Python installation.

# to create it in windows we write: py -m venv .venv
# Decoding:
# py
# │
# └── Run Python
# -m
# │
# └── Run a Python module
# venv
# │
# └── The module that creates virtual environments
# .venv
# │
# └── Name of the folder we're creating
#but in macOS it would be: python -m venv .venv

#to activate it in windows we would write:.\.venv\Scripts\Activate.ps14
#to activate it in macOS we weould write: source .venv/bin/activate
#Windows → Scripts
# macOS   → bin
# And Windows uses \ in paths:
# .venv\Scripts
# while macOS normally uses /:
# .venv/bin

#If it works, you'll notice something new at the beginning of your terminal:
# (.venv) PS D:\AI Automation journey\Week 3\Day 20>
# That:
# (.venv)
# 
# is VERY important. It means:
# 🟢 "Any Python packages I install now belong to this virtual environment."

#to turn off the environment you simply write: deactivate

#if you send someone an app, and it needs certain pachages instead of sendin them with it you can:
#python -m pip freeze: shows you the installed packages and versions
#python -m pip freeze > requirements.txt: saves the output of python -m pip freeze to a file 
# the person who recieves the app you will also send the reqauirements.txt file to him
#and he will write in the powershell terminal
#python -m pip install -r requirements.txt

#freeze > requirements.txt
#         = SAVE my package setup 📝
# 
# install -r requirements.txt
#         = REBUILD my package setup 🔨