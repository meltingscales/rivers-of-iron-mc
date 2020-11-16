import argparse
import json
from typing import Dict, List, Tuple, Union
from pprint import pprint

dummy_obj = {
    "projectID": None,
    "fileID": None,
    "required": True
}

json_filepath='rivers-of-iron/manifest.json'


parser = argparse.ArgumentParser()

parser.add_argument(
    '-f', "--fileid", required=True, metavar=int,
    help="FileID in CurseForge. Example of one (3040523): https://www.curseforge.com/minecraft/mc-mods/jei/download/3040523/file")

parser.add_argument(
    "-p", '--projectid', required=True, metavar=int,
    help="Project ID in CurseForge. Example of one (238222): https://www.curseforge.com/minecraft/mc-mods/jei")

args = parser.parse_args()


with open(json_filepath) as f:
    jsonobj: Dict[str, Union[Dict, List]] = json.load(f)

dummy_obj['projectID']=int(args.projectid)
dummy_obj['fileID']=int(args.fileid)

jsonobj['files'].append(dummy_obj)

pprint(jsonobj['files'][-1])

with open(json_filepath, 'w+') as f:
    f.write(json.dumps(jsonobj, indent=2))
    