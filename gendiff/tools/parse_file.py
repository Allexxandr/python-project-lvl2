
import json
from pathlib import Path


def get_dict_from_file(path_file):
    file_extension = Path(path_file).suffix
    return open_file(path_file, file_extension)


def open_file(path_file, file_extension):
    if file_extension.lower() == '.json':
        return json.load(open(path_file))
