#!/usr/bin/ebv python3

with open("invictus.txt") as f:
    next(f) #skip the first line of file
    for line in f:
        print(line.rstrip())
