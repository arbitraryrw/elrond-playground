import json
import os

class Util():

    def __init__(self):
        pass

    @staticmethod
    def deserialise_json_file(json_file_path: str) -> dict:
        # Weak file check, simply check file extension is json..
        if json_file_path[-5:] != ".json":
            return None

        if not os.path.isfile(json_file_path):
            return None

        with open(json_file_path) as file:
            data = json.load(file)
        
        return data
    
    @staticmethod
    def pretty_format_json(json_string: str) -> str:
        return json.dumps(json_string, indent=4, sort_keys=True)
