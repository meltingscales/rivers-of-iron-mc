import os

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
