import sys

from string_abbreviation.abbreviation import generate_abbreviations


class AbbreviationLibrary:

    def __init__(self):

        self.word_to_abb = {}
        self.abb_to_word = {}
        self.compressed_sentence = []

    def get_raw_compressed(self):
        return self.compressed_sentence

    def append(self, words):
        for word in words:
            if word in self.word_to_abb:
                self.compressed_sentence.append(self.word_to_abb[word])
                continue

            abbreviations = generate_abbreviations(word)
            for abbreviation in abbreviations:
                if abbreviation not in self.abb_to_word:
                    self.word_to_abb[word] = abbreviation
                    self.abb_to_word[abbreviation] = word
                    self.compressed_sentence.append(abbreviation)
                    break

    def decompress(self):
        decompress_sentence = []
        for abb in self.compressed_sentence:
            decompress_sentence.append(self.abb_to_word[abb])

        return ' '.join(decompress_sentence).replace('  ', ' ').strip()

    def replace(self, word, replacement):
        # get abbreviation of the word
        abb = self.word_to_abb.get(word)
        if not abb:
            return

        # remove the word from word_to_abb
        self.word_to_abb.pop(word)

        if replacement not in self.word_to_abb:
            self.word_to_abb[replacement] = abb

        self.abb_to_word[abb] = replacement

    def delete(self, word):
        self.replace(word, "")


def main():

    sample_word = 'duck'
    sample_abbreviations = generate_abbreviations(sample_word)
    print(f'The word {sample_word} has the following possible abbreviations in the order of preferred use.')
    print(sample_abbreviations)
    print()
    print()

    try:
        abb_lib = AbbreviationLibrary()
        abb_lib.append(['nobody', 'cares', 'how', 'it', 'works', 'as', 'long', 'as', 'it', 'works'])

        print(abb_lib.get_raw_compressed())

        print(abb_lib.decompress())

        abb_lib.replace("it", 'something')
        print(abb_lib.decompress())

        abb_lib.delete('how')
        print(abb_lib.decompress())

    except NotImplementedError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()

