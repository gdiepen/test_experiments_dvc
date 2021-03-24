import yaml
import json

with open("params.yaml") as f:
    settings = yaml.safe_load(f)["settings"]

    x = settings["x"]
    y = settings["y"]

with open("metrics.json", "w") as f:
    f.write(json.dumps({"product": x * y}))
