import logging
from collections import defaultdict
from collections import deque
from itertools import product
from typing import List, Optional


class WordLadder:
    """
    The class for solving 'word ladder' problem, that states to find a way
    to transform one word into another with only one letter change in each step.

    :param words_list: List of words that search should be done
    """

    def __init__(self, words_list: List[str]):
        if not words_list:
            logging.error("Can't initialize with empty dictionary words")
            raise ValueError("Can't initialize with empty dictionary words")

        self.words = words_list
        self.words_buckets = defaultdict(list)
        self.graph = defaultdict(set)

        self._generate_words_list()
        self._build_word_graph()

    def _generate_words_list(self) -> None:
        logging.debug("Starting to generate words buckets")
        for word in self.words:
            for i in range(len(word)):
                word_bucket = f"{word[:i]}_{word[i + 1:]}"
                self.words_buckets[word_bucket].append(word)

    def _build_word_graph(self) -> None:
        logging.debug("Starting to build words graph")
        for bucket, mutual_neighbors in self.words_buckets.items():
            underscore_idx = bucket.index("_")

            for word1, word2 in product(mutual_neighbors, repeat=2):
                if self._one_letter_diff(word1[underscore_idx], word2[underscore_idx]):
                    self.graph[word1].add(word2)
                    self.graph[word2].add(word1)

    @staticmethod
    def _same_case(char1: str, char2: str) -> bool:
        """
        Checks if 2 chars are the same case (either upper or lower).

        :param char1: First char to check
        :param char2: Second char to check
        :return: Whether both of chars are the same case
        :rtype: bool
        """
        return (char1.islower() and char2.islower() or
                char1.isupper() and char2.isupper())

    def _one_letter_diff(self, char1: str, char2: str) -> bool:
        """
        Checks if 2 chars can be considered as 1-step transformation from
        char1 to char2. There are two possible cases: different chars in
        the same case or same char with difference in case.

        :param char1: First char to check
        :param char2: Second char to check
        :return: Whether chars can be changed in 1 step
        :rtype: bool
        """
        return ((self._same_case(char1, char2) and char1 != char2) or
                (not self._same_case(char1, char2) and char1.swapcase() == char2))

    def traverse(self, start_word: str, end_word: str) -> List[Optional[str]]:
        """
        Perform the algorithm to get chain of transformation from start_word to
        end_word with 1-letter difference in each step.
        If such path isn't found, empty list will be returned.

        :param start_word: Start word of the chain
        :param end_word: End word of the chain
        :return: List of changes needed to get end_word from start_word
        :rtype: List[str]
        """
        if start_word == "" or end_word == "":
            logging.warning("Empty strings were supplied")
            return []

        logging.info("Starting to traverse through present graph")
        visited = set()
        queue = deque([[start_word]])

        while queue:
            path = queue.popleft()
            vertex = path[-1]

            if vertex == end_word:
                logging.debug("Found path for %s and %s", start_word, end_word)
                return path

            for neighbor in self.graph[vertex] - visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

        logging.warning("Path hasn't been found for %s and %s", start_word, end_word)
        return []
