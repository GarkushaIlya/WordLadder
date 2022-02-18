import pytest

from wordladder.arg_parser import ArgParser

CIRCLE_GRAPH_WORDS = [
    "buuz", "nuuz", "neuz", "neez", "neer", "beer", "buer", "buur"
]
STAR_GRAPH_WORDS = [
    "vane", "vans", "vale", "vine", "sane"
]
DISCONNECTED_GRAPH_WORDS = [
    "test", "noxs", "boer", "qiun", "opox", "boom"
]
RANDOM_GRAPH_WORDS = [
    "kane", "lane", "vane", "vans", "lone", "lont", "loxe", "loxn",
    "moxe", "toxe", "Toxe", "ToXe", "TOXe", "taxe", "taxi"
]
DUPLICATES_GRAPH_WORDS = [
    "taxi", "taxi", "toxi"
]


@pytest.fixture
def arg_parser(tmpdir):
    ArgParser._start = 'test'
    ArgParser._end = 'ssss'
    ArgParser._input_file = 'tests_assets/test.txt'
    ArgParser._output_file = tmpdir.join('out.txt')

    return ArgParser
