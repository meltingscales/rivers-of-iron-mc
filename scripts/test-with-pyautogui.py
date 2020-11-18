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


def is_multimc(p: Process) -> bool:
    ismmc = False

    name, cmdline = "", ""

    try:
        name = p.name()
        cmdline = p.cmdline()
    except (PermissionError, psutil.AccessDenied) as e:  # Windows can do this
        # print("Not allowed to view process {}".format(p.pid))
        pass

    # print(name, cmdline)

    if 'MultiMC' in name or 'MultiMC' in ' '.join(cmdline):
        # if 'MultiMC' in name:
        print(p)
        ismmc = True

    return ismmc


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


def focus_multimc() -> BaseWindow:

    w: BaseWindow = gw.getWindowsWithTitle(get_multimc_window_title())[0]
    w.activate()
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
    time.sleep(10)

    mmc_window = focus_multimc()

    '''
    <ESC>
    Add instance
    Import from zip
    paste path
    click on ok
    wait for import
    launch
    wait and check for main menu, wait for crashes
    terminate mmc
    exit 0 or 1!
    '''

    # time.sleep(10)
    # mmc_proc.kill() # kill MMC after 10s for testing
    print("killed mmc.")

    exit(1)
