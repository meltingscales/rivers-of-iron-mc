from pprint import pprint
import distutils.spawn
from config import DEFAULT_ZIP_NAME, MMC_BINARY_PATHS, ZIP_NAME
import psutil
import subprocess
import shutil
import os
import time
from pygetwindow import BaseWindow
import pygetwindow as gw
import pyautogui as pag
from psutil import Process
from os import remove
import platform
import timeit


def is_windows():
    return platform.system() == 'Windows'


def is_vm():
    if is_windows():
        wmic_output = subprocess.check_output(
            ['wmic', 'bios', 'get', 'serialnumber'], shell=True)
        wmic_output = wmic_output.decode()
        wmic_output = wmic_output.replace('SerialNumber', '')
        wmic_output = wmic_output.strip()

        return wmic_output == '0'
    else:
        raise Exception(
            "Checking if I'm in a VM is not implemented for Linux.")


def cycle_windows_backwards():
    """Alt shift tab."""
    pag.hotkey("alt", "shift", "tab")


def altf4():
    """Alt-F4."""
    pag.hotkey('alt', 'f4')


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
    # if 'MultiMC' in name:
    if 'multimc' in name.lower() or 'multimc' in ' '.join(cmdline).lower():
        print(p)
        return True

    return False


def remove_file(fp):
    if os.path.exists(fp):
        os.remove(fp)


def get_multimc_binary_path():
    for path in MMC_BINARY_PATHS:
        if os.path.exists(path):
            return path
    return None


def get_multimc_instances_path():
    multimc_instances_folder = os.path.join(
        os.path.dirname(get_multimc_binary_path()), 'instances')
    if not os.path.exists(multimc_instances_folder):
        raise Exception(
            "MMC Instances folder, {}, does not exist! Halting.", multimc_instances_folder)

    return multimc_instances_folder


def ensure_packwiz_installed():
    if not distutils.spawn.find_executable("packwiz"):
        raise Exception(
            "`packwiz` not found on PATH. Download from https://github.com/comp500/packwiz")


def ensure_multimc_installed():
    if not get_multimc_binary_path():
        print("Could not find MultiMC binary. Searched these paths:")
        pprint(MMC_BINARY_PATHS)
        raise Exception("Could not find MMC instance.")


def ensure_multimc_closed():
    # multimc must be closed
    multimc_open = False
    for p in psutil.process_iter():
        multimc_open = is_multimc(p)

    if multimc_open:
        raise Exception("MultiMC must be CLOSED for this to work.")


def open_multimc() -> subprocess.Popen:
    path = get_multimc_binary_path()
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
