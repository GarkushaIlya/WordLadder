from unittest import mock

import pytest

from wordladder.words_reader import WordFileWorker


@pytest.mark.parametrize("read_data, expected", [
    ("test, tess, tsss, ssss", ["test", "tess", "tsss", "ssss"]),
    ("TEST, xzxq, tGfX", ["TEST", "xzxq", "tGfX"]),
])
def test_read_words(arg_parser, read_data, expected):
    mock_open = mock.mock_open(read_data=read_data)

    with mock.patch('builtins.open', mock_open):
        result = WordFileWorker.read_words()

    assert type(result) is list
    assert len(result) == len(expected)
    assert result == expected


@pytest.mark.parametrize("word_chain, expected", [
    (['test', 'tess', 'tsss', 'ssss'], "test, tess, tsss, ssss"),
    ([], "test -x-> ssss")
])
def test_file_save(arg_parser, word_chain, expected):
    WordFileWorker.save_chain(word_chain)

    with open(arg_parser.output_file(), 'r') as file:
        written_data = file.read()
        assert written_data == expected
