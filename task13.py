import xml.etree.ElementTree as etree


class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self):
        tree = etree.parse('annot.opcorpora.no_ambig.xml')
        root = tree.getroot()
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

    def get_sentence(self, num_sent):
        if num_sent < 1:
            raise ValueError("Номер предложения не может быть меньше 1.")
        else:
            return self._sentences[num_sent-1]._sent
            #print(self._sentences[num_sent-1].sent)

    def get_word(self, num_sent, num_word):
        return self._sentences[num_sent-1]._wordforms[num_word-1]._wordform
        #print(self._sentences[num_sent-1]._wordforms[num_word-1].wordform)

    def get_grammems(self, num_sent, num_word, num_gram):
        return self._sentences[num_sent-1]._wordforms[num_word-1]._grammems[num_gram-1]
        #print(self._sentences[num_sent-1]._wordforms[num_word-1]._grammems[num_gram-1])


class Sentence:

    def __init__(self, sent, wordforms):
        self._wordforms = wordforms
        self._sent = sent

    def get_wordforms(self):
        return self._wordforms

    def get_sent(self):
        return self._sent


class Wordform:
    def __init__(self, wordform, grammems):
        self._grammems = grammems
        self._wordform = wordform

    def get_gramms(self):
        return self._grammems

    def get_wordform(self):
        return self._wordform
