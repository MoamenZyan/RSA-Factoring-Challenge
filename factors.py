#!/usr/bin/python3
import sys
with open(sys.argv[1], "r") as file:
    content = file.readlines()

for i in range(len(content)):
    if int(content[i][:-1]) % 2 == 0:
        print(f"{int(content[i])} = {int(int(content[i]) / 2)}*2")

    if int(content[i][:-1]) % 3 == 0:
        print(f"{int(content[i])} = {int(int(content[i]) / 3)}*3")
