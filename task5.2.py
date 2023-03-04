import json
import collections
from collections import defaultdict

defdict = collections.defaultdict(list)
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                defdict[action['character']].append(action['says'])

print(defdict)