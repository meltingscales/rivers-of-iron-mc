import pyautogui
import os
import psutil
import distutils.spawn
import platform
from pprint import pprint

IS_WINDOWS = platform.system() == 'Windows'

LINUX_MMC_PATHS = [
    '/opt/multimc/run.sh',
]

WINDOWS_MMC_PATHS = [
    'C:/tools/MultiMC/MultiMC.exe',
    'C:/Program Files (x86)/MultiMC/MultiMC.exe'
    'C:/Program Files/MultiMC/MultiMC.exe'
]

def get_multimc_path():
    if IS_WINDOWS:
        for path in WINDOWS_MMC_PATHS:
            if os.path.exists(path):
                return path
    else:
        for path in LINUX_MMC_PATHS:
            if os.path.exists(path):
                return path
    return None

def ensure_packwiz_installed():
    if not distutils.spawn.find_executable("packwiz"):
        raise Exception(
            "`packwiz` not found on PATH. Download from https://github.com/comp500/packwiz")


def ensure_multimc_installed():
    if not get_multimc_path():
        print("Could not find MultiMC instance. Searched these paths:")
        pprint(LINUX_MMC_PATHS)
        pprint(WINDOWS_MMC_PATHS)
        raise Exception("Could not find MMC instance.")

def ensure_multimc_closed():
    # multimc must be closed
    multimc_open = False
    for p in psutil.process_iter():

        name, cmdline = "", ""

        try:
            name = p.name()
            cmdline = p.cmdline()
        except (PermissionError, psutil.AccessDenied) as e:  # Windows can do this
            # print("Not allowed to view process {}".format(p.pid))
            pass

        # print(name, cmdline)

        if 'MultiMC' in name or 'MultiMC' in ' '.join(cmdline):
            print(p)
            multimc_open = True

    if multimc_open:
        raise Exception("MultiMC must be CLOSED for this to work.")


def open_multimc():
    path = get_multimc_path()
    print("Exec {}".format(path))
    os.system(path)

if __name__ == '__main__':
    ensure_packwiz_installed()
    ensure_multimc_installed()

    ensure_multimc_closed()
    open_multimc()

    '''
    <ESC>
    Add instance
    Import from zip
    run `packwiz cf export`
    paste path
    click on ok
    wait for import
    launch
    wait and check for main menu, wait for crashes
    terminate mmc
    exit 0 or 1!
    '''