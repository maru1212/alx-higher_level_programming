#!/usr/bin/python3
def element_at(mylist, idx):
    if idx >= 0 and len(mylist) > idx:
        return(mylist[idx])
    else:
        return("None")
