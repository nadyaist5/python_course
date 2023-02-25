import json

with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    with open("dict2.txt", "w") as g:
        for act in data["acts"]:
            for scene in act["scenes"]:
                characters = []
                for action in scene["action"]:
                    if action["character"] in characters:
                        continue
                    else:
                        characters.append(action["character"])
                g.write(json.dumps(characters, sort_keys=False, indent=4))