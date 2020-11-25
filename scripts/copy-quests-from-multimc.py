import glob
import os
import shutil

PATH_GLOBS = [
    'C:/tools/MultiMC/instances/rivers-of-iro*/minecraft/config/ftbquests',
    # TODO linux
]

LOCAL_CONFIG_PATH = './config/ftbquests'


def merge_folders(src, dest) -> int:
    # https://stackoverflow.com/questions/22588225/how-do-you-merge-two-directories-or-move-with-replace-from-the-windows-command
    '''
    Updates destenation root, overwrites existing files.
    :param sourceRoot: Root folder from wehere to copy the files
    :param destRoot: Destination folder where new folders and files are created and new files are added
    :return: !=0 in case of errors
    '''
    if not os.path.exists(dest):
        return 1
    ok = 0
    for path, dirs, files in os.walk(src):
        relPath = os.path.relpath(path, src)
        destPath = os.path.join(dest, relPath)
        if not os.path.exists(destPath):
            print("create: %s" % destPath)
            os.makedirs(destPath)
        for file in files:
            destFile = os.path.join(destPath, file)
            if os.path.isfile(destFile):
                print("\n...Will overwrite existing file: " +
                      os.path.join(relPath, file))
                #ok = False
                # continue
            srcFile = os.path.join(path, file)
            # print "rename", srcFile, destFile
            # os.rename(srcFile, destFile) # performs move
            print("copy %s to %s" % (srcFile, destFile))
            shutil.copy(srcFile, destFile)  # performs copy&overwrite
    return ok


def get_ftbquests_path() -> str:
    for pathglob in PATH_GLOBS:

        paths = glob.glob(pathglob)
        print(paths)

        if len(paths) > 1:
            print(paths)
            raise Exception("More than 1 path! Aborting!", paths)
        if len(paths) == 1:
            p = paths[0]
            if(os.path.exists(p)):
                return p
            else:
                raise Exception("path does not exist!",p)

    raise Exception("No paths were valid: ", PATH_GLOBS)


if __name__ == '__main__':
    if os.path.exists(LOCAL_CONFIG_PATH):
        merge_folders(get_ftbquests_path(), LOCAL_CONFIG_PATH)
    else:
        raise Exception("Could not find path " +
                        os.path.abspath(LOCAL_CONFIG_PATH))
