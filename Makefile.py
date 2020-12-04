import os
import shutil
import subprocess
from subprocess import CalledProcessError


def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()


def get_latest_git_tag():
    try:
        return subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()
    except CalledProcessError as e: # They don't have tags... Not really an issue.
        return "v???"


subprocess.check_output(["packwiz", "cf", "export"])

outzip = f'rivers-of-iron-latest-{get_latest_git_tag()}-{get_git_revision_short_hash()}.zip'

shutil.move('Rivers of Iron.zip', outzip)

print(f"Enjoy your pack at {outzip}")
