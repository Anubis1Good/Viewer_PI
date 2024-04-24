import shutil
import os
import winreg
path = 'C:\Program Files (x86)\Viewer_PI'
if os.path.exists(path):
    shutil.rmtree(path)

key_name = 'viewer_PI'

key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,f'*\\shell\\{key_name}',access=winreg.KEY_SET_VALUE)
winreg.DeleteKey(key,"command")
winreg.DeleteKey(key,"")

