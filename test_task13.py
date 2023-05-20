import xml.etree.ElementTree as etree
import unittest
from task13 import Corpus


class CorpusTest(unittest.TestCase):

    def setUp(self):
        self.corpus = Corpus()
        self.corpus.load()

        tree = etree.parse('annot.opcorpora.no_ambig.xml')
        root = tree.getroot()

        self.test_corpus = []
        for sentence in root.findall('text/paragraphs/paragraph/sentence'):
            sent = sentence.find('source').text
            words = []
            for token in sentence.iter('token'):
                wordform = token.get('text')
                grammems = []
                for g in token.iter('g'):
                    grammems.append(g.attrib['v'])
                word = [wordform, grammems]
                words.append(word)
            sentence = [sent, words]
            self.test_corpus.append(sentence)

    def test_num_sents(self):
        self.assertEqual(len(self.test_corpus), len(self.corpus._sentences))

    def test_sentences(self):
        for i in range(len(self.corpus._sentences)):
            sent_1 = self.corpus._sentences[i].sent
            sent_2 = self.test_corpus[i][0]
            self.assertEqual(sent_1, sent_2)

    def test_words(self):
        for i in range(len(self.corpus._sentences)):
            sent_1 = self.corpus._sentences[i]._wordforms
            sent_2 = self.test_corpus[i][1]
            wordCount = len(sent_1)
            for j in range(wordCount):
                self.assertEqual(sent_1[j].wordform, sent_2[j][0])

    def test_grammems(self):
        for i in range(len(self.corpus._sentences)):
            sent_1 = self.corpus._sentences[i]._wordforms
            sent_2 = self.test_corpus[i][1]
            wordCount = len(sent_1)
            for j in range(wordCount):
                word_1 = sent_1[j]._grammems
                word_2 = sent_2[j][1]
                grammemCount = len(word_1)
                for k in range(grammemCount):
                    self.assertEqual(word_1[k], word_2[k])


if __name__ == '__main__':
    unittest.main()
    