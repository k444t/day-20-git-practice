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

