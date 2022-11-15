import json
import toml


def get_json(file):
    with open(f"src/data/{file}.json", "r") as f:
        return json.load(f)[file]


def get_meta():
    with open("pyproject.toml", "r") as f:
        f = toml.load(f)["tool"]["poetry"]
        return {
            "name": f["name"],
            "version": "v" + f["version"],
            "description": f["description"],
            "license": {
                "name": f["license"],
                "url": "https://github.com/Vyvy-vi/attendance-management-system/blob/master/LICENSE.md",
            },
            "repo": f["repository"],
            "author": {"name": "Vyom Jain", "url": "https://github.com/Vyvy-vi"},
        }
