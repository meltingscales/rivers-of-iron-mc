import pyautogui
import os
import psutil
import distutils.spawn

def ensure_packwiz():
    if distutils.spawn.find_executable("packwiz") is None:
        raise Exception("`packwiz` not found on PATH. Download from https://github.com/comp500/packwiz")

def ensure_mmc_closed():        
    # multimc must be closed
    multimc_open=False
    for p in psutil.process_iter():
        if 'MultiMC' in p.name() or 'MultiMC' in ' '.join(p.cmdline()):
            print(p)
            multimc_open=True

    if multimc_open:
        raise Exception("MultiMC must be CLOSED for this to work.")



if __name__ == '__main__':
    ensure_packwiz()

    ensure_mmc_closed()