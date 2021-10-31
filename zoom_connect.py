import os
import subprocess
import keyboard
from time import sleep

if (os.name != 'nt'):
    print('sorry, Windows only')
    quit()

APPDATA = os.getenv('APPDATA')
conf = ['', '', '', [], ''] # conf_no, pwd, hash_pwd, day, start_time

def url_create(conf_no, hash_pwd):
    url = APPDATA + '\\Zoom\\bin\\Zoom.exe' + \
          ' --url="zoommtg://zoom.us/join?action=join&confno=' + \
          conf_no
    if hash_pwd:
        url += '&pwd=' + hash_pwd
    url += '"'
    # print(url)
    return url

def run_zoom(conf_no, pwd, hash_pwd=None):
    url = url_create(conf_no, hash_pwd)
    # print('zoommtg')
    subprocess.Popen(url)
    if hash_pwd is None:
        sleep(7)
        # print('pwd')
        keyboard.write(pwd)
        sleep(1)
        # print('enter')
        keyboard.send('Tab, Space')

room = ['############', '####']
# subprocess.run(APPDATA + '\\Zoom\\bin\\Zoom.exe')
# sleep(3)

run_zoom(*room)
