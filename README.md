# Preparation

# Rules

Your program should calculate the shortest list of four-letter words, starting with StartWord, and ending with EndWord,
with a number of intermediate words that must appear in the DictionaryFile file where each word differs from the
previous word by one letter only. The result should be written to the destination specified by the ResultFile argument.

For example, if StartWord = Spin, EndWord = Spot and DictionaryFile file contains Spin Spit Spat Spot Span

then ResultFile should contain Spin Spit Spot

Two examples of incorrect results:
Spin, Span, Spat, Spot (incorrect as it takes 3 changes rather than 2)
Spin, Spon, Spot (incorrect as spon is not a word)

# Run commands

To run use  `python wordladder/main.py start_word end_word words_file output_file`

Example: `python wordladder/main.py test ssss test.txt out.txt`, result can be found in out.txt

Also `setuptools` can be used in order to start an application. To do so go to a folder with `setup.py` file and run
this command: `pip install .`. After that you can get rid of the command with python and simply run it with the
following: `word_ladder start_word end_word words_file output_file`

# Algorithm for word chain search

For build and search of a word chain were used words buckets and BFS respectively.

For each word there is a bucket, that represented as `t_es`, where underscore is all possible chars in this position, so
that such bucket shows common words with difference only in this particular position. For example _beer_ and
_bear_ will be in `'be_r'` bucket and so on. In such fashion all words in a given dictionary file are iterated and all
possible buckets are created.

Those buckets are used for next step: building a graph of adjacent words, where adjacency represents change of 1 letter
in any position so that _word1_ transforms into _word2_. After such manipulations BFS is come in play. Chain of
transformations from _word1_ to _word2_ with 1-letter difference in each step can be represented as a graph, where each
node is a word from the dictionary and edges are possible transformation from _word_x_ to _word_y_. I have chosen BFS
because we need to ensure that such path is the shortest one and BFS can do such favor for us. BFS is applied to our a
class instance that holds graph of the given words.

Another point that worth to mention is that search can be improved with next heuristics: search can be start from both
start and end, so such searches will meet each other in the middle.

## Structure of code

For this solution I used SOLID principles and OOP. So that every class has only one responsibility and should be easily
tested with unit test. So that classes don't heavily rely on each other implementation. A main class is `WordLadder`
with its implementation of building graph and performing BFS. Also, there are utility classes as `ArgParser`
and `WordFileWorker`. This separation was made to make it easily testable and extendable. `WordLadder` can be extended
to serve multiple searches, known as online-task solving. As for other algorithm, that used for search the class can be
modified or inherited for implementation of other approach or even _Strategy_ architecture pattern can be handy. For
testing purposes is used pytest.

## Assumptions that are made

- Given input file with words is comma separated list of words like follows: _test, Size, maTe, TEXT_
- Given words from input file are correct and comply to a restriction of size (four-letter words) and content (only
  upper\lower case letters)
- If the given words are both or either of them not in the dictionary, any exceptions won't be raised (if they are valid
  in terms of length and chars) and result will be as listed: `word1 -x-> word2`
- Output file can be named as user wants it to be, but its extension should end with _.txt_