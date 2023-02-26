import json

with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    characters = {}
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                if action["character"] in characters:
                    characters[action["character"]] += 1
                else:
                    characters[action["character"]] = 0
max = -1
name = ''
for character in characters:
    if characters[character] > max:
        max = characters[character]
        name = character
print(name)