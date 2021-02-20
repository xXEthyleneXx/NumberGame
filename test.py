import os, urllib.request, pathlib, time, subprocess, random


def main():

    def doupdate():
        home = os.path.expanduser("~")
        os.chdir(home)
        dlurl = "https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/u.txt"
        path = str(home) + "/u.txt"
        try:
            os.remove('u.txt')
        except FileNotFoundError:
            print('Its Not Here')
        urllib.request.urlretrieve(dlurl, '{}'.format(path))
        U = open('u.txt', 'r')
        update = U.readline(0)
        print(update)

    doupdate()
main()