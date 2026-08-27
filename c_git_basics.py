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
#U beside a file means untracked
#A beside a file means added / staged

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

pritn("learning git")