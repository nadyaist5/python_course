import json

with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    data = []
    for row in f:
        data.append(json.loads(row))
    dictionary = {}
    for obj in data:
        word = obj["label"]["value"]
        try:
            dictionary[word] = obj["description"]["value"]
        except KeyError:
            dictionary[word] = 'None'

with open("dict.json", "w", encoding='utf-8') as g:
    json.dump(dictionary, g, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))