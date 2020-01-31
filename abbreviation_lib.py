import sys
from typing import List

from string_abbreviation.abbreviation import generate_abbreviations


class AbbreviationLibrary:

    def __init__(self):
        pass

    def get_raw_compressed(self) -> List[str]:
        """
        Return the compressed words in memory in the order they were appended.
        Returns:
            List[str]: List of compressed words in the order they were appended
        """
        raise NotImplementedError("get_raw_compressed not implemented")

    def append(self, words: List[str]) -> None:
        """
        Compress each word in the list words and save in the order they were entered.
        If append is called multiple times, the previously saved compressed words must retain their order
        Args:
            words (List[str): List of words which are to be compressed

        Returns:
            None
        """
        raise NotImplementedError("append not implemented")

    def decompress(self) -> List[str]:
        """
        Decompress the compressed words in memory and return them in order of entry.
        Returns:
            List[str]: Decompressed words in order of entry.
        """
        raise NotImplementedError("decompress not implemented")

    def replace(self, word: str, replacement: str) -> None:
        """
        Replace a word with the replacement.
        For example, replace('dock', 'duck') will replace dock with duck when the saved compressed words
        are decompressed and printed.
        Args:
            word (str): Word to replace
            replacement (str): Word to replace with

        Returns:
            None

        """
        raise NotImplementedError("replace not implemented")

    def delete(self, word: str) -> None:
        """
        Delete a word from the compressed collection
        For example, delete('duck') will delete duck such that when the saved compressed words
        are decompressed and printed, duck is not printed if it was ever appended previously.
        Args:
            word (str): Word to delete

        Returns:
            None

        """
        raise NotImplementedError("delete not implemented")


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
