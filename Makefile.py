import os
import shutil
import subprocess


def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()


def get_latest_git_tag():
    return subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()


subprocess.check_output(["packwiz", "cf", "export"])

outzip = f'rivers-of-iron-latest-{get_latest_git_tag()}-{get_git_revision_short_hash()}.zip'

shutil.move('export.zip', outzip)

print(f"Enjoy your pack at {outzip}")
