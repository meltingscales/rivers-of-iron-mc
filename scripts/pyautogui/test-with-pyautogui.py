'''
Test the modpack by launching MultiMC, importing and running the pack.

Exits with different error codes depending on what went wrong.
'''
from pprint import pprint
import distutils.spawn
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

IS_WINDOWS = platform.system() == 'Windows'
wmic_output = subprocess.check_output(
    ['wmic', 'bios', 'get', 'serialnumber'], shell=True)
wmic_output = wmic_output.decode()
wmic_output = wmic_output.replace('SerialNumber', '')
wmic_output = wmic_output.strip()

IS_VM = False  # TODO linux
if IS_WINDOWS:
    IS_VM = (wmic_output == '0')

if IS_VM:
    print("We are running in a VM!")
else:
    print("We are not running in a VM!")

MODPACK_NAME = '.TMP.PYAUTOGUI-TEST-MODPACK-EXPORT.tmp'
ZIP_NAME = MODPACK_NAME+'.zip'
DEFAULT_ZIP_NAME = 'export.zip'

SCRIPTS_FOLDER = 'scripts/pyautogui'


def png_path(fp):
    return os.path.join(SCRIPTS_FOLDER, fp)


MMC_BINARY_PATHS = [
    '/opt/multimc/run.sh',

    'C:/tools/MultiMC/MultiMC.exe',
    'C:/Program Files (x86)/MultiMC/MultiMC.exe',
    'C:/Program Files/MultiMC/MultiMC.exe',
]


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


if __name__ == '__main__':
    ensure_packwiz_installed()
    ensure_multimc_installed()

    ensure_multimc_closed()
    generate_modpack_zip()

    mmc_proc = open_multimc()
    time.sleep(2)  # wait for mmc to open

    mmc_window = get_multimc_window()
    # mmc_window.activate() # Also doesn't focus... Crashes.

    # Our focused window is NOT 'MultiMC'...SHIFT-ALT-TAB.
    if 'multimc' not in gw.getActiveWindow().title.lower():
        print("Not seeing MultiMC. Alt-Shift-Tab in 1 second.")
        time.sleep(1)
        cycle_windows_backwards()

    # Our focused window is STILL NOT 'MultiMC'...Abort.
    if 'multimc' not in gw.getActiveWindow().title.lower():
        raise Exception("NOT FOCUSED ON MultiMC! Aborting. Currently focused window: {}".format(
            gw.getActiveWindow().title.lower()))

    pag.press('esc')  # close any initial dialogues

    # This very critical code ensures the kitty is always activated.
    location = pag.locateOnScreen(png_path('kitty-disabled.png'))
    if location:
        print("Enabling kitty.")
        pag.click(location)
    else:
        print("Kitty already enabled.")

    # TODO: Delete old instances if they exist.
    multimc_instances_folder = get_multimc_instances_path()

    old_pack_folder = os.path.join(multimc_instances_folder, MODPACK_NAME)
    if os.path.exists(old_pack_folder):
        print("Deleting old pack folder {}.".format(old_pack_folder))
        shutil.rmtree(old_pack_folder)
    else:
        print("No old pack folder detected.")

    location = pag.locateOnScreen(png_path('add-instance.png'))
    if not location:
        raise Exception("Could not add instance!")
    pag.click(location)

    # get to import from zip screen
    pag.press(['tab', 'tab', 'tab', 'down'], interval=0.5)

    pag.press(['tab', 'tab'], interval=0.5)  # to focus text box

    pag.typewrite(os.path.realpath(ZIP_NAME))  # enter path

    pag.press('enter')
    time.sleep(20)


    # Window says "Please wait..."
    n = 5
    time.sleep(n)
    print("Waiting for modpack install.")
    while True:
        if 'please wait' in gw.getActiveWindow().title.lower():
            print("Window is telling me to wait, I think I will...")
        else:
            print("We're done waiting! Modpack installed.")
            break
        time.sleep(n)
    time.sleep(n)

    # launch
    location = pag.locateOnScreen(png_path('launch.png'))
    if not location:
        raise Exception("Could not launch pack!")
    pag.click(location)

    # detect minecraft window name and start counting
    print("Waiting for modpack to load...")
    n = 5
    time.sleep(n)
    while True:
        if 'minecraft' in gw.getActiveWindow().title.lower():
            print("Minecraft window has been opened!")

            print("Timer started!")
            START_TIME = time.time()

            break
        else:
            print("Waiting {} seconds for minecraft window...".format(n))
        time.sleep(n)

    # detect mojang logo on loading screen
    print("Waiting for loading screen to show up...")
    n = 5
    time.sleep(n)
    while True:
        if pag.locateOnScreen(png_path('mojang-logo.png')):
            print("Mojang logo visible!")
            break
        else:
            print("Waiting {} seconds for mojang logo...".format(n))
        time.sleep(n)

    # detect java logo in title
    print("Waiting for 'Java' logo in title...")
    n = 5
    time.sleep(n)
    while True:
        if pag.locateOnScreen(png_path('java.png')):
            print("Java logo visible! We're on the main menu!")

            END_TIME = time.time()
            print("Timer ended.")

            break
        else:
            print("Waiting {} seconds for Java logo...".format(n))
        time.sleep(n)

    TIME_TO_LOAD_INTO_MAIN_MENU = (END_TIME - START_TIME)
    print("Pack took {:.2f} sec or {:.2f} min to load.".format(
        TIME_TO_LOAD_INTO_MAIN_MENU, TIME_TO_LOAD_INTO_MAIN_MENU/60))

    print("killing mmc in 5s...")
    time.sleep(5)
    mmc_proc.kill()  # kill MMC after 10s for testing
    print("killed mmc.")

    print("killing minecraft in 5s...")
    time.sleep(5)
    active_window = gw.getActiveWindow()
    if 'minecraft 1.' in active_window.title.lower():
        print("ALT-F4 on MC Window...")
        altf4()
    else:
        raise Exception(
            "Minecraft 1.* window is not focused! Cannot close it.")
