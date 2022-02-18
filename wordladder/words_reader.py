import logging
from string import ascii_letters
from typing import List

from wordladder.arg_parser import ArgParser


class WordFileWorker:
    """
    The utility class for loading a list of the words from the file.
    """

    @classmethod
    def read_words(cls) -> List[str]:
        """
        Load words list from the given file. Words should be separated
        with comma and whitespace.

        :return: List of words
        :rtype: List[str]
        """
        with open(ArgParser.input_file(), "r", encoding="utf8") as f_handler:
            words_str = f_handler.read()
            words_list = words_str.split(", ")
            logging.info("Words load is successful")
            return words_list

    @classmethod
    def save_chain(cls, words_chain: List[str]) -> None:
        """
        Save word chain as 'word1, word2, ..., wordx'. If such chain isn't found,
        will be saved 'start_word -x-> end_word'.

        :param words_chain: List of words to save as result
        :return: None
        """
        result = (
            ", ".join(words_chain) if words_chain
            else (ArgParser.start() + " -x-> " + ArgParser.end())
        )
        with open(ArgParser.output_file(), "w", encoding="utf8") as f_handler:
            f_handler.write(result)

        logging.info("Result saved to %s", ArgParser.output_file())
