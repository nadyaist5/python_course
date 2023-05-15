import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()


class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self):
        for sentence in root.findall('text/paragraphs/paragraph/sentence'):
            sent = sentence.find('source').text
            words = []
            for token in sentence.iter('token'):
                wordform = token.get('text')
                grammems = []
                for g in token.iter('g'):
                    grammems.append(g.attrib['v'])
                word = Wordform(wordform, grammems)
                words.append(word)
            sentence = Sentence(sent, words)
            self._sentences.append(sentence)

        #print(len(self._sentences))

    def get_sentence(self, num_sent):
        if num_sent < 1:
            raise ValueError("Номер предложения не может быть меньше 1.")
        else:
            print(self._sentences[num_sent-1].sent)

    def get_word(self, num_sent, num_word):
        print(self._sentences[num_sent-1]._wordforms[num_word-1].wordform)

    def get_grammems(self, num_sent, num_word, num_gram):
        print(self._sentences[num_sent-1]._wordforms[num_word-1]._grammems[num_gram-1])


class Sentence:

    def __init__(self, sent, wordforms):
        self._wordforms = wordforms
        self.sent = sent


class Wordform:
    def __init__(self, wordform, grammems):
        self._grammems = grammems
        self.wordform = wordform


num1 = Corpus()
num1.load()
num1.get_sentence(4)
num1.get_word(4, 3)
num1.get_grammems(4, 3, 1)