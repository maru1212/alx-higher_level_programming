#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 0:
        print("{:d}".format(n))
    else:
        add = 0
        for x in range(1, n):
            add += int(sys.argv[x])
        print("{:d}".format(add))
