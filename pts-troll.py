#!/usr/bin/python3
import os
import sys

def get_own_tty():
    tty_name = os.ttyname(sys.stdout.fileno())
    tty_num = tty_name.split("/")[3]
    return tty_num

def main():
    own_tty = get_own_tty()
    other_tty = [tty for tty in os.listdir("/dev/pts") if tty not in [own_tty, "ptmx"]]
    for tty_num in other_tty:
        os.system("cat duck_ascii.txt > /dev/pts/{}".format(tty_num))
    #print(other_tty)



if __name__ == "__main__":
    main()
