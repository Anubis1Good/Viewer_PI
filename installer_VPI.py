import os
import shutil
import winreg
programm = 'Viewer_Pi.exe'
icon = 'Viewer_PI.ico'
path = 'C:\Program Files (x86)\Viewer_PI'
if not os.path.exists(path):
    os.makedirs(path)
    shutil.copy(programm,path)
    shutil.copy(icon,path)

key_name = 'viewer_PI'
key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,'*\\shell')
winreg.CreateKey(key,key_name)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,f'*\\shell\\{key_name}',access=winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'icon', 0, winreg.REG_SZ, '"C:\\Program Files (x86)\\Viewer_PI\\Viewer_PI.ico"')
winreg.SetValue(key, 'command', winreg.REG_SZ, '"C:\\Program Files (x86)\\Viewer_PI\\Viewer_PI.exe" "%1"')
winreg.CloseKey(key)
