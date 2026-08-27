#Think of Git as a save-history system for your code.
#It lets you create checkpoints so you can see what changed or return to an older version.

#Git basically has three important stages:
# Working directory
#       ↓
#    git add
#       ↓
# Staging area
#       ↓
#   git commit
#       ↓
# Git history
# Imagine you're playing a game:
# Working directory = you're currently playing and making changes.
# Staging area = you've chosen exactly what you want included in your next save.
# Commit = you actually create the save point.
# So when you ran:
# git add .
# you didn't save a checkpoint yet.
# You told Git:
# "These are the files I want in my next checkpoint."

#to save a checkpont you would write:git commit -m "Day 20: virtual environments and Git basics"
#git commit
#     ↓
# Create a checkpoint

# -m
#     ↓
# I'm providing a message/name for the checkpoint

# "Day 20: virtual environments and Git basics"
#     ↓
# Description of what this checkpoint contains

#if it's your first time doin so ona laptop you will get:
#Author identity unknown
# Please tell me who you are.
#that's normal

#when you make the check point you will get a feedback this is what it means:
#master → your current Git branch.
# root-commit → this is the first commit in this repository.
# b7ae779 → the unique ID for this commit.
# 5 files changed → Git saved changes from 5 files.
# 39 insertions(+) → 39 lines were added.

#git init: initialises git

#git add .
# The . means:
# Add everything in the current folder that isn't ignored.
# Because .venv/ is in .gitignore, Git will not add it.

#git commit -m "message": creates a checkpoint

#git log oneline: shows me the checkpoints
#it wil give us something like this:
#b7ae779 (HEAD -> master) Day 20: Virtual environment and Git basics
# │        │      │       │
# │        │      │       └── Your commit message
# │        │      └────────── You're on the "master" branch
# │        └───────────────── HEAD = where you currently are
# └────────────────────────── Commit ID

#One important distinction before we continue: Git is local. Nothing has been uploaded to GitHub yet. 
#Right now, the checkpoint exists only on your laptop

# git status: shows me the status of the files and if anything has been modified
#untracked → Git has never tracked this file
# modified  → Git knows this file, but it changed
# staged    → change is selected for the next commit
# committed → checkpoint has been saved
#U beside a file means untracked
#A beside a file means added / staged
#M beside a file means modifies

#git diff → What exactly changed inside those files?
#to exit from it after showing you what changed simply press "q"

#to restore to the previous checkpoint:
#use git status
#write: git restore (The file that chaged but dont write the paransthesis)

#What if you've already staged the change?
# There's an important difference. Suppose you modify a file and then do:
# git add c_git_basics.py
# Now the change is staged. If you decide, “Wait, I don't want this in my next commit,” 
# you can unstage it without deleting your work:
# git restore --staged c_git_basics.py
# This does not undo your code. It only removes the file from the staging area:

# to connect git to github we ca use: git remote add origin 'the link of the repository'
# git remote add origin <GitHub address>
#       │       │
#       │       └── nickname for this GitHub repository
#       │
#       └── add a remote connection

#we will be adding the files to github by git push -u origin main
#git push -u origin main
#          │    │     │
#          |    |  main: the branch you want to push
#          |   origin: the nickname for your GitHub repository/remote connection
#          -u: remember this connection for future pushes

#So the first time:
# git push -u origin main
# Git learns:
# my local main
#      ↓
# origin/main on GitHub
# After that, you can usually just write:
# git push
# instead of:
# git push origin main

#we can rename the branch by git branch -M main
#git branch
#     │
#     └── work with branches

# -M
#  │
#  └── rename the current branch

# main
#  │
#  └── new branch name

print("learning")