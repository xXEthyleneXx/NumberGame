# Updates the checker to the latest version
def main():
    def download():
        import os, urllib.request, pathlib
        home = os.path.expanduser("~")
        os.chdir(home)
        dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/checker.py'
        path = str(home) + '\checker.pyw'
        try:
            os.remove('checker.pyw')
        except FileNotFoundError:
            print('Its Not Here')
        urllib.request.urlretrieve(dlurl, '{}'.format(path))
        os.system("start cmd /c {}".format('py ' + path))
        quit()
    download()
main()