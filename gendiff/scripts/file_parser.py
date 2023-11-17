import json
import yaml


def open_file(file_path):
    with open(file_path) as handle:
        if file_path[-4:] == 'json':
            file = json.loads(handle.read())
        if file_path[-4:] == 'yaml' or file_path[-3:] == 'yml':
            file = yaml.safe_load(handle.read())
    return(file)

