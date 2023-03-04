import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('nouns_plur.txt', 'w', encoding='utf-8') as f:
    for word in root.findall('text/paragraphs/paragraph/sentence/tokens/token'):
        noun_flag = 0
        plur_flag = 0
        for g in word.iter('g'):
            if g.attrib['v'] == "NOUN":
                noun_flag = 1
            if g.attrib['v'] == "plur":
                plur_flag = 1
        if noun_flag == 1 and plur_flag == 1:
            f.write(word.attrib['text'])
            f.write('\n')