from unittest import TestCase

from string_abbreviation.abbreviation_lib import AbbreviationLibrary
#from string_abbreviation.abbreviation_lib_solution import AbbreviationLibrary


class TestIntegration(TestCase):

    def setUp(self):
        self.abbreviation_lib = AbbreviationLibrary()

        self.large_sentence = ['australia', 'officially', 'the', 'commonwealth', 'of', 'australia', 'is', 'a',
                               'sovereign', 'country',
                               'comprising', 'the', 'mainland', 'of', 'the', 'australian', 'continent', 'the', 'island',
                               'of', 'tasmania',
                               'and', 'numerous', 'smaller', 'islands', 'it', 'is', 'the', 'largest', 'country', 'in',
                               'oceania', 'and',
                               'the', 'worlds', 'sixth', 'largest', 'country', 'by', 'total', 'area']

    def test_empty_string_decompress(self):
        self.abbreviation_lib.append([''])
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('', actual)

    def test_single_string_decompress(self):
        self.abbreviation_lib.append(['qsic'])
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('qsic', actual)

    def test_sentence_decompress(self):
        self.abbreviation_lib.append(['this', 'is', 'a', 'test', 'sentence', 'to', 'see', 'if', 'this', 'works'])
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('this is a test sentence to see if this works', actual)

    def test_empty_string_replacement(self):
        self.abbreviation_lib.append([''])
        self.abbreviation_lib.replace('', 'qsic')
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('', actual)

    def test_single_string_replacement(self):
        self.abbreviation_lib.append(['foo'])
        self.abbreviation_lib.replace('foo', 'qsic')
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('qsic', actual)

    def test_sentence_replacement(self):
        self.abbreviation_lib.append(['this', 'is', 'a', 'test', 'sentence', 'to', 'see', 'if', 'this', 'works'])
        self.abbreviation_lib.replace('this', 'qsic')
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('qsic is a test sentence to see if qsic works', actual)

    def test_empty_string_delete(self):
        self.abbreviation_lib.append([''])
        self.abbreviation_lib.delete('')
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('', actual)

    def test_single_string_delete(self):
        self.abbreviation_lib.append(['foo'])
        self.abbreviation_lib.delete('foo')
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('', actual)

    def test_sentence_delete(self):
        self.abbreviation_lib.append(['this', 'is', 'a', 'test', 'sentence', 'to', 'see', 'if', 'this', 'works'])
        self.abbreviation_lib.delete('this')
        actual = self.abbreviation_lib.decompress()
        self.assertEqual('is a test sentence to see if works', actual)

    def test_empty_string_compressed(self):
        self.abbreviation_lib.append([''])
        actual = self.abbreviation_lib.get_raw_compressed()
        self.assertEqual([], actual)

    def test_single_string_compressed(self):
        self.abbreviation_lib.append(['foo'])
        actual = self.abbreviation_lib.get_raw_compressed()
        self.assertEqual(['3'], actual)

    def test_sentence_compressed(self):
        self.abbreviation_lib.append(['this', 'is', 'a', 'test', 'sentence', 'to', 'see', 'if', 'this', 'works'])
        actual = self.abbreviation_lib.get_raw_compressed()
        self.assertEqual(['4', '2', '1', '3t', '8', '1o', '3', '1f', '4', '5'], actual)

    def test_large_sentence_decompression(self):
        self.abbreviation_lib.append(self.large_sentence)
        actual = self.abbreviation_lib.decompress()
        self.assertEqual(' '.join(self.large_sentence).replace('  ', ' ').strip(), actual)

    def test_large_sentence_replacement(self):
        self.abbreviation_lib.append(self.large_sentence)
        self.abbreviation_lib.replace('the', 'of')
        actual = self.abbreviation_lib.decompress()
        expected = 'australia officially of commonwealth of australia is a sovereign country comprising of mainland ' \
                   'of of australian continent of island of tasmania and numerous smaller islands it is of largest ' \
                   'country in oceania and of worlds sixth largest country by total area'
        self.assertEqual(expected, actual)

    def test_large_sentence_delete(self):
        self.abbreviation_lib.append(self.large_sentence)
        self.abbreviation_lib.delete('the')
        actual = self.abbreviation_lib.decompress()
        expected = 'australia officially commonwealth of australia is a sovereign country comprising mainland of ' \
                   'australian continent island of tasmania and numerous smaller islands it is largest country in ' \
                   'oceania and worlds sixth largest country by total area'
        self.assertEqual(expected, actual)

    def test_large_sentence_compressed(self):
        self.abbreviation_lib.append(self.large_sentence)
        actual = self.abbreviation_lib.get_raw_compressed()
        expected = ['9', '10', '3', '12', '2', '9', '1s', '1', '8n', '7', '9g', '3', '8', '2', '3', '9n', '8t', '3',
                    '6', '2', '7a', '2d', '7s', '6r', '6s', '1t', '1s', '3', '6t', '7', '1n', '6a', '2d', '3', '5s',
                    '5', '6t', '7', '1y', '4l', '4']
        self.assertEqual(expected, actual)
