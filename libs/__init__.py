import json
import os.path


def load_config(file):
    root_path = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(root_path, file)
    with open(config_file) as f:
        conf = json.load(f)
    return conf
