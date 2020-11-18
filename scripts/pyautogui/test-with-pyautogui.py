'''
Test the modpack by launching MultiMC, importing and running the pack.

Exits with different error codes depending on what went wrong.
'''
from pprint import pprint
import distutils.spawn
import psutil
import subprocess
import os
import time
from pygetwindow import BaseWindow
import pygetwindow as gw
import pyautogui as pag
from psutil import Process
from os import remove
import platform

IS_WINDOWS = platform.system() == 'Windows'


ZIP_NAME = '.PYAUTOGUI-TEST-MODPACK-EXPORT.tmp.zip'
DEFAULT_ZIP_NAME = 'export.zip'

MMC_PATHS = [
    '/opt/multimc/run.sh',

    'C:/tools/MultiMC/MultiMC.exe',
    'C:/Program Files (x86)/MultiMC/MultiMC.exe',
    'C:/Program Files/MultiMC/MultiMC.exe',
]

def cycle_windows_backwards():
    """Alt shift tab."""
    pag.keyDown('alt') 
    pag.keyDown('shift')
    pag.press('tab')

    pag.keyUp('alt') 
    pag.keyUp('shift')



def is_multimc(p: Process) -> bool:
    ismmc = False

    name, cmdline = "", ""

    try:
        name = p.name()
        cmdline = p.cmdline()
    except (PermissionError, psutil.AccessDenied) as e:  # Windows can do this
        print("Not allowed to view process {}".format(p.pid))
        pass

    # print(name, cmdline)
    # if 'MultiMC' in name:
    if 'multimc' in name.lower() or 'multimc' in ' '.join(cmdline).lower():
        print(p)
        return True

    return False


def remove_file(fp):
    if os.path.exists(fp):
        os.remove(fp)


def get_multimc_path():
    for path in MMC_PATHS:
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
        pprint(MMC_PATHS)
        raise Exception("Could not find MMC instance.")


def ensure_multimc_closed():
    # multimc must be closed
    multimc_open = False
    for p in psutil.process_iter():
        multimc_open = is_multimc(p)

    if multimc_open:
        raise Exception("MultiMC must be CLOSED for this to work.")


def open_multimc() -> subprocess.Popen:
    path = get_multimc_path()
    print("Exec {} in background".format(path))
    # os.system(path) # NOTE: this blocks.
    return subprocess.Popen([path])

def get_multimc_window_title() -> str:
    windowTitles = gw.getAllTitles()

    for title in windowTitles:
        if 'multimc' in title.lower():
            print(title)
            return title

    pprint(windowTitles)
    raise Exception("Could not find window title containing 'MultiMC'!")


def get_multimc_window() -> BaseWindow:
    w: BaseWindow = gw.getWindowsWithTitle(get_multimc_window_title())[0]
    pprint(w)
    return w


def generate_modpack_zip():

    print("Generating modpack zip at "+ZIP_NAME)
    if not os.path.exists("./pack.toml"):
        raise Exception(
            "Could not find pack.toml in current working directory '{}'!".format(os.getcwd()))

    remove_file(ZIP_NAME)
    remove_file(DEFAULT_ZIP_NAME)

    subprocess.check_output(['packwiz', 'cf', 'export'])
    print("Done!")

    os.rename(DEFAULT_ZIP_NAME, ZIP_NAME)


if __name__ == '__main__':
    ensure_packwiz_installed()
    ensure_multimc_installed()

    ensure_multimc_closed()
    generate_modpack_zip()

    mmc_proc = open_multimc()
    time.sleep(3) # wait 3s for mmc to open

    mmc_window = get_multimc_window()
    # mmc_window.activate() # Also doesn't focus... Crashes.


    # Our focused window is NOT 'MultiMC'...SHIFT-ALT-TAB.
    if 'multimc' not in gw.getActiveWindow().title.lower():
        print("Not seeing MultiMC. Alt-Shift-Tab in 1 second.")
        time.sleep(1)
        cycle_windows_backwards()

    # Our focused window is STILL NOT 'MultiMC'...Abort.
    if 'multimc' not in gw.getActiveWindow().title.lower():
        raise Exception("NOT FOCUSED ON MultiMC! Aborting. Currently focused window: {}".format(gw.getActiveWindow().title.lower()))

    pag.press('esc') #close any initial dialogues

    # TODO press kitty
    

    # TODO Add instance
    # TODO Import from zip
    # TODO paste path
    # TODO click on ok
    # TODO wait for import
    # TODO launch
    # TODO wait and check for main menu, wait for crashes


    print("killing mmc in 10s...")
    time.sleep(10)
    mmc_proc.kill() # kill MMC after 10s for testing
    print("killed mmc.")

    exit(1)
