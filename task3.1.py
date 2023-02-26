import json

with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    dictionary = {}
    for row in f:
        line = json.loads(row)
        word = line["label"]["value"]
        try:
            dictionary[word] = line["description"]["value"]
        except KeyError:
            dictionary[word] = 'None'

with open("dict.json", "w", encoding='utf-8') as g:
    json.dump(dictionary, g, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
