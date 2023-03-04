import json
import collections
from collections import Counter

list_of_words = []
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                for speech in action["says"]:
                    speech = speech.lower()
                    speech = speech.replace(',', '')
                    speech = speech.replace(';', '')
                    speech = speech.replace(':', '')
                    speech = speech.replace('!', '')
                    speech = speech.replace('?', '')
                    speech = speech.replace('.', '')
                    list_of_words = list_of_words + speech.split(' ')

print('20 самых частых слов:')
for word in Counter(list_of_words).most_common(20):
    print(word[0])
print('20 самых редких слов:')
for word in Counter(list_of_words).most_common()[:-20:-1]:
    print(word[0])
