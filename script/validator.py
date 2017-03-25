from jsonschema import validate
import glob
import yaml
import json
import sys
import os

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    root = os.path.join(path, "../")

    for f in glob.glob(root + "*.schema"):
        print(f)
        with open(f, 'r') as s:
            schema = json.load(s)

        file = os.path.splitext(f)[0]
        for g in ["yml", "yaml", "json"]:
            val_file = "{}.{}".format(file, g)
            if os.path.isfile(val_file):
                with open(val_file, 'r') as stream:            
                    validate(yaml.load(stream), schema)

if __name__ == "__main__":
    main()