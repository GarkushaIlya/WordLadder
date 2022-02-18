import argparse
import sys
from unittest import mock

import pytest

from wordladder.arg_parser import ArgParser


@pytest.mark.parametrize("word", [
    "test",
    "eeee",
    "zxVT",
])
def test_word_checker_correct_input(word):
    ArgParser.word_checker(word)


@pytest.mark.parametrize("word", [
    "tes.",
    "    ",
    "tests",
    "TTEST",
    "%est",
    "/~zz",
    "тест",
    "000W",
    "t  e",
    "t\te",
    "-=("
])
def test_word_checker_incorrect_input_punctuation_and_length(word):
    with pytest.raises(argparse.ArgumentTypeError):
        ArgParser.word_checker(word)


@pytest.mark.parametrize("sys_args_list", [
    (["", "test", "fide", "input.txt", "output.txt"]),
    (["", "MoSt", "DIZY", "some_text.txt", "enormous_file-name.txt"])
])
def test_arg_parser_parse_args(sys_args_list):
    ArgParser._start = None
    ArgParser._end = None
    ArgParser._input_file = None
    ArgParser._output_file = None

    with mock.patch.object(sys, 'argv', sys_args_list):
        with mock.patch('os.path.exists') as exists:
            exists.return_value = True

            assert ArgParser.start() == sys_args_list[1]
            assert ArgParser.end() == sys_args_list[2]
            assert ArgParser.input_file() == sys_args_list[3]
            assert ArgParser.output_file() == sys_args_list[4]


@pytest.mark.parametrize("sys_args_list, input_file_exists", [
    (["", "testi", "fide", "test.txt", "output.txt"], True),
    (["", "tes~", "fide", "test.txt", "output.txt"], True),
    (["", "test", "Flide", "test.txt", "output.txt"], True),
    (["", "test", "%ide", "test.txt", "output.txt"], True),
    (["", "&XXX", "~de~", "test.txt", "output.txt"], False),
    (["", "test", "test", "test.txt", "output.tx"], True),
    (["", "test", "test", "test.txt", "output"], True),
    (["", "test", "test", "test.txt", ""], True),
])
def test_arg_parser_incorrect_input(sys_args_list, input_file_exists):
    with mock.patch.object(sys, 'argv', sys_args_list):
        with mock.patch('os.path.exists') as exists:
            exists.return_value = input_file_exists

            try:
                ArgParser.get_parsed_args()
            except SystemExit as e:
                assert isinstance(e.__context__, argparse.ArgumentError)
            else:
                raise ValueError("Exception not raised")
