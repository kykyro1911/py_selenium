import json

with open("cfg.json") as a:
    b = json.load(a)

print(b['name_'][1])
