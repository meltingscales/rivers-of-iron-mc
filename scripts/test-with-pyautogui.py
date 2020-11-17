import pyautogui
import os
import psutil
import distutils.spawn
import platform

IS_WINDOWS = platform.system() == 'Windows'

def ensure_packwiz():    
    if not distutils.spawn.find_executable("packwiz"):
        raise Exception("`packwiz` not found on PATH. Download from https://github.com/comp500/packwiz")

def ensure_mmc_closed():        
    # multimc must be closed
    multimc_open=False
    for p in psutil.process_iter():
        
        name, cmdline="",""

        try:
            name = p.name()
            cmdline=p.cmdline()
        except (PermissionError,psutil.AccessDenied) as e: # Windows can do this
            # print("Not allowed to view process {}".format(p.pid))
            pass

        # print(name, cmdline)

        if 'MultiMC' in name or 'MultiMC' in ' '.join(cmdline):
            print(p)
            multimc_open=True

    if multimc_open:
        raise Exception("MultiMC must be CLOSED for this to work.")

def open_multimc():
    pass #TODO


if __name__ == '__main__':
    ensure_packwiz()

    ensure_mmc_closed()