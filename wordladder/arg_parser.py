import argparse
import logging
import os
from string import ascii_letters
from typing import Optional


class ArgParser:
    """
    The utility class for parsing command arguments from the console.
    """
    _start = None
    _end = None
    _input_file = None
    _output_file = None

    @classmethod
    def word_checker(cls, word: str) -> Optional[str]:
        """
        Checks whether a given word is valid with respect to present restrictions.

        :param word: Given word to check
        :return: Word if it is valid
        :rtype: str
        """
        logging.debug("Start parsing of start/end param. Given: %s", word)
        if len(word) == 4 and all(char in ascii_letters for char in word):
            return word

        logging.error("Wrong start/end word was given: %s. Aborting", word)
        raise argparse.ArgumentTypeError(
            "The word must be four-letter word without "
            "punctuation and whitespace symbols"
        )

    @classmethod
    def input_file_checker(cls, path: str) -> Optional[str]:
        """
        Checks whether a given input file path is valid.

        :param path: Given path to check
        :return: Path if it is valid
        :rtype: str
        """
        logging.debug("Start parsing of input file")
        if os.path.exists(os.path.join(os.getcwd(), path)):
            return path

        logging.error("Wrong input file name was given: %s. Aborting", path)
        raise argparse.ArgumentTypeError(f"No such file or directory: {path}")

    @classmethod
    def output_file_checker(cls, path: str) -> Optional[str]:
        """
        Checks whether a given output file path is valid.

        :param path: Given path to check
        :return: Path if it is valid
        :rtype: str
        """
        logging.debug("Start parsing of start param")
        if path.endswith(".txt"):
            return path

        logging.error("Wrong output file name was given: %s. Aborting", path)
        raise argparse.ArgumentTypeError(f"Illegal file name: {path}")

    @classmethod
    def get_parsed_args(cls):
        """
        Parses command arguments from a console input.

        :return: None
        """
        logging.debug("Start parsing of start param")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "start",
            type=cls.word_checker,
            help="The start word."
        )
        parser.add_argument(
            "end",
            type=cls.word_checker,
            help="The end word."
        )
        parser.add_argument(
            "input_file",
            type=cls.input_file_checker,
            help="The file name of a text file containing four letter words."
        )
        parser.add_argument(
            "output_file",
            type=cls.output_file_checker,
            help="The file name of a text file that will contain the result."
        )

        args = parser.parse_args()
        cls._start = args.start
        cls._end = args.end
        cls._input_file = args.input_file
        cls._output_file = args.output_file

        logging.info("Successfully parsed console params")

    @classmethod
    def start(cls):
        """
        Parsed command argument from console. Represents start word.

        :return: Start word
        :rtype: str
        """
        if cls._start is None:
            cls.get_parsed_args()

        return cls._start

    @classmethod
    def end(cls):
        """
        Parsed command argument from console. Represents end word.

        :return: End word
        :rtype: str
        """
        if cls._end is None:
            cls.get_parsed_args()

        return cls._end

    @classmethod
    def input_file(cls) -> str:
        """
        Parsed command argument from console. Represents input file with words.

        :return: Input file
        :rtype: str
        """
        if cls._input_file is None:
            cls.get_parsed_args()

        return cls._input_file

    @classmethod
    def output_file(cls):
        """
        Parsed command argument from console. Represents output file to write a result.

        :return: Output file
        :rtype: str
        """
        if cls._output_file is None:
            cls.get_parsed_args()

        return cls._output_file
