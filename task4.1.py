import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('sentences.txt', 'w', encoding='utf-8') as f:
    for sentence in root.findall('text/paragraphs/paragraph/sentence/source'):
        f.write(sentence.text)
        f.write('\n')