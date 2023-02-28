import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

conj = 0
verb = 0
for word in root.findall('text/paragraphs/paragraph/sentence/tokens/token'):
    if word.attrib['text'] == 'может' or word.attrib['text'] == 'Может':
        for g in word.iter('g'):
            if g.attrib['v'] == "CONJ":
                conj += 1
            if g.attrib['v'] == "VERB":
                verb += 1
print('Слово "может" встречается как союз', conj, 'раз')
print('Слово "может" встречается как глагол', verb, 'раз')
