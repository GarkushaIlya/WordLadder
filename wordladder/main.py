import logging
import logging.config

from wordladder.arg_parser import ArgParser
from wordladder.word_ladder import WordLadder
from wordladder.words_reader import WordFileWorker


def main():
    """
    The main entry point to run the application calculating
     the shortest list of four-letter words.
    """
    logging.basicConfig(
        filename='application.log',
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(filename)s]: %(message)s"
    )
    logging.info("Start of main module")

    words_list = WordFileWorker.read_words()
    word_ladder = WordLadder(words_list)
    word_chain = word_ladder.traverse(ArgParser.start(), ArgParser.end())

    WordFileWorker.save_chain(word_chain)
    logging.info("Finish of main module")


if __name__ == '__main__':
    main()
