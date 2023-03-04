import json
import collections

cnt = collections.Counter()
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                cnt[action['character']] += 1
print(cnt)