import pytest

from tests.conftest import (CIRCLE_GRAPH_WORDS, STAR_GRAPH_WORDS,
                            DISCONNECTED_GRAPH_WORDS, RANDOM_GRAPH_WORDS,
                            DUPLICATES_GRAPH_WORDS)
from wordladder.word_ladder import WordLadder


@pytest.mark.parametrize("words, expected", [
    (["test", "task"],
     {"_ask": ["task"],
      "_est": ["test"],
      "t_sk": ["task"],
      "t_st": ["test"],
      "ta_k": ["task"],
      "tas_": ["task"],
      "te_t": ["test"],
      "tes_": ["test"]}
     ),
    (["mark", "hark"],
     {"_ark": ["mark", "hark"],
      "h_rk": ["hark"],
      "ha_k": ["hark"],
      "har_": ["hark"],
      "m_rk": ["mark"],
      "ma_k": ["mark"],
      "mar_": ["mark"]}
     ),
    (["test", "Test", "mist"],
     {"T_st": ["Test"],
      "Te_t": ["Test"],
      "Tes_": ["Test"],
      "_est": ["test", "Test"],
      "_ist": ["mist"],
      "m_st": ["mist"],
      "mi_t": ["mist"],
      "mis_": ["mist"],
      "t_st": ["test"],
      "te_t": ["test"],
      "tes_": ["test"]}
     )
])
def test_word_ladder_words_buckets(arg_parser, words, expected):
    word_ladder = WordLadder(words)

    assert word_ladder.words_buckets == expected


@pytest.mark.parametrize("words, expected", [
    (["mane", "mone", "xone", "zone"],
     {"mane": {"mone"},
      "mone": {"xone", "zone", "mane"},
      "xone": {"mone", "zone"},
      "zone": {"mone", "xone"}
      }),
    (["mane", "mone", "pone", "poni"],
     {"mane": {"mone"},
      "mone": {"mane", "pone"},
      "pone": {"mone", "poni"},
      "poni": {"pone"}
      }),
    (["beer", "neer", "boer", "beir", "been"],
     {"beer": {"neer", "boer", "beir", "been"},
      "neer": {"beer"},
      "boer": {"beer"},
      "beir": {"beer"},
      "been": {"beer"}
      })
])
def test_word_ladder_build_graph(words, expected):
    word_ladder = WordLadder(words)

    assert word_ladder.graph == expected


@pytest.mark.parametrize("words_list, start, end, expected", [
    (CIRCLE_GRAPH_WORDS, "buuz", "beer",
     ['buuz', 'buur', 'buer', 'beer']),
    (STAR_GRAPH_WORDS, "sane", "vale",
     ['sane', 'vane', 'vale']),
    (STAR_GRAPH_WORDS, "vane", "vine",
     ["vane", "vine"]),
    (RANDOM_GRAPH_WORDS, "taxi", "vans",
     ["taxi", "taxe", "toxe", "loxe", "lone", "lane", "vane", "vans"]),
    (RANDOM_GRAPH_WORDS, "taxi", "TOXe",
     ["taxi", "taxe", "toxe", "Toxe", "ToXe", "TOXe"]),
    (RANDOM_GRAPH_WORDS, "TOXe", "taxi",
     ['TOXe', 'ToXe', 'Toxe', 'toxe', 'taxe', 'taxi']),
    (DISCONNECTED_GRAPH_WORDS, "boom", "noxs",
     [])
])
def test_word_ladder_traverse(words_list, start, end, expected):
    word_ladder = WordLadder(words_list)
    word_chain = word_ladder.traverse(start, end)

    assert word_chain == expected


@pytest.mark.parametrize("words_list, start, end, expected", [
    (DUPLICATES_GRAPH_WORDS, "taxi", "taxi", ["taxi"]),
    (DUPLICATES_GRAPH_WORDS, "taxi", "toxi", ["taxi", "toxi"]),
    (DUPLICATES_GRAPH_WORDS, "taxi", "maxi", []),
    (DUPLICATES_GRAPH_WORDS, "maxi", "taxi", []),
    (DUPLICATES_GRAPH_WORDS, "", "taxi", []),
    (DUPLICATES_GRAPH_WORDS, "taxi", "", []),
    (DUPLICATES_GRAPH_WORDS, "", "", []),
])
def test_word_ladder_traverse_incorrect(words_list, start, end, expected):
    word_ladder = WordLadder(words_list)
    word_chain = word_ladder.traverse(start, end)

    assert word_chain == expected


def test_word_ladder_traverse_empty_words():
    with pytest.raises(ValueError):
        WordLadder([])
