#!/usr/bin/python3

def islower(c):
    for alpha in range(ord('a'), ord('z') + 1):
        if c == chr(alpha):
            return(True)
        elif c != chr(alpha) and chr(alpha) == "z":
            return(False)
