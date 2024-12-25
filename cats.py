"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"

    # return [paragraphs[k] for element in paragraphs if select(paragraphs[k])]
    # return paragraphs[k] if select(paragraphs[k]) else ''


    # att 2
    #     if select(paragraphs[i])
    # for i in range(k, len(paragraphs)):
    #     if select(paragraphs[i]):
    #         return paragraphs[i]
    # return ''


    # att 3
    i = -1
    for element in paragraphs:
        if select(element):
            i += 1
        if i == k:
            return element
    return ''

    # END PROBLEM 1

# ps = ['short', 'really long', 'tiny']
# s = lambda p: len(p) <= 5
# print(pick(ps, s, 2))


def about(subject):
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def select_func(element):
        paragraph_word_list = split(remove_punctuation(lower(element)))
        for subject_element in subject:
            for each_word in paragraph_word_list:
                if subject_element == each_word:
                    return True
        return False

                # return subject_element != each_word
                # if subject_element != each_word:

        #     return lower(element) != lower(subject_element)
        # return True

        # return lower(element) smething lower(subject)

    return select_func

    # END PROBLEM 2

# example return function
# def f(element):
#     # return len(element) <= 4
#     return True

def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"

    # if len(source_words) > len(typed_words):
    #     source_words = source_words[:len(typed_words)-1]

    if len(source_words) == 0 and len(typed_words) == 0:
        return 100.0

    winned_pts = 0
    # for i in range(len(typed_words) if len(typed_words) < len(source_words) else len(source_words)):
    for i in range(len(source_words) if len(source_words) < len(typed_words) else len(typed_words)):
        if typed_words[i] == source_words[i]:
            winned_pts += 1
    # total_possible_pts = len(typed_words) if len(typed_words) > len(source_words) else len(source_words)
    total_possible_pts = len(typed_words)
    
    if len(typed_words) == 1 and len(source_words) == 1:
        if typed_words == source_words:
            return 100.0
    if len(typed_words) == 0:
        return 0.0

    return 0.0 if len(source_words) == 0 else winned_pts / total_possible_pts * 100

    # END PROBLEM 3

# print(accuracy("a b c d", "a d"))

def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"

    return len(typed) / 5 / (elapsed / 60)

    # END PROBLEM 4

# print(wpm("", 10))


############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    def length_diff(w1, w2):
        return min(abs(len(w2) - len(w1)))

    for a_word in word_list:
        if typed_word == a_word:
            return typed_word

    # lowest_diff = limit
    # lowest_diff_word = ''
    # for a_word in word_list:
    #     # if diff_function(typed_word, a_word, limit) <= lowest_diff:
    #     difference = diff_function(typed_word, a_word, limit) 
    #     if difference <= lowest_diff:
    #         lowest_diff = diff_function(typed_word, a_word, limit)
    #         lowest_diff_word = a_word
    # return typed_word if lowest_diff_word == '' else lowest_diff_word
    
    # attempt 2
    min_difference = 100000
    possible_word = ''
    for a_word in word_list:
        difference = diff_function(typed_word, a_word, limit)
        if difference < min_difference:
            min_difference = difference
            possible_word = a_word

    if min_difference > limit:
        return typed_word

    return possible_word

    # END PROBLEM 5

# print(autocorrect('stilter', ['modernizer', 'posticum', 'undiscernible', 'heterotrophic', 'waller', 'marque', 'dephosphorization'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1))


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'

    if len(typed) == 0:
        return len(source)
    elif len(source) == 0:
        return len(typed)
    elif limit <= -1:
        return 0

    if typed[0] != source[0]:
        return feline_fixes(typed[1:], source[1:], limit - 1) + 1
    else:
        return feline_fixes(typed[1:], source[1:], limit)

    # END PROBLEM 6

# print(feline_fixes("someaweqwertyuio", "awesomeasdfghjkl", 3))

############
# Phase 2B #
############


def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # if typed == source:
    #     return 0
    # elif typed != source:
    #     return 1

    # elif typed[0] != source[0]:
    #     return minimum_mewtations(typed, source[1:], limit)
    # elif False:
    #     minimum_mewtations(typed)
    # elif typed != source:
    #     return 1
        




    # if typed[0] == source[0]:
    #     return minimum_mewtations(typed[1:], source[1:], limit)
    # if len(typed[0]) > len(source[0]):
    #     return minimum_mewtations(typed[1:], source, limit)
    # if len(typed[0]) < len(source[0]):
    #     return minimum_mewtations(typed, source[1:], limit)


    if limit < 0:
        return 0
    if len(typed) == 0: # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(source)
        # END
    if len(source) == 0:
        return len(typed)
    if typed == source:
        return 0
    if typed[0] == source[0]:
        return minimum_mewtations(typed[1:], source[1:], limit)

    
    # Recursive cases should go below here
    else:
        add = minimum_mewtations(typed, source[1:], limit - 1)
        remove = minimum_mewtations(typed[1:], source, limit - 1)
        substitute = minimum_mewtations(typed[1:], source[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"

    return 1 + min(add, remove, substitute)    

    # if len(typed) < len(source):
    #     return add + 1
    # if len(typed) > len(source):
    #     return remove + 1
    # if typed[0] != source[0]: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     return substitute + 1
        # END
 



    # if len(typed) == 0:
    #     return len(source)
    # if len(source) == 0:
    #     return len(typed)
    # if typed == source:
    #     return 0
    
    # if typed[0] != source[0]:
    #     return minimum_mewtations(typed[1:], source[1:], limit) + 1
    # if typed[0] == source[0]:
    #     return minimum_mewtations(typed[1:], source[1:], limit)

    # # if len(typed[0]) < len(source[0]):        wtf was i doing
    # if len(typed) < len(source):
    #     return minimum_mewtations(typed, source[1:], limit) + 1

    # if len(typed) > len(source):
    #     return minimum_mewtations(typed[1:], source, limit) + 1


# print(minimum_mewtations("speling", "spelling", big_limit))
# print(minimum_mewtations("wird", "twird", big_limit))

# print(minimum_mewtations('ab', 'ac', 100))



    # assert False, 'Remove this line'
    # if ___________: # Base cases should go here, you may add more base cases as needed.
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END
    # # Recursive cases should go below here
    # if ___________: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END
    # else:
    #     add = ... # Fill in these lines
    #     remove = ...
    #     substitute = ...
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'

FINAL_DIFF_LIMIT = 6 # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"

    correct = 0
    while correct < len(typed) and typed[correct] == source[correct]:
        correct += 1
    
    progress = correct / len(source)
    upload({'id': user_id, 'progress': progress})
    return progress


    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    absolute_times = []
    for player_times in timestamps_per_player:
        temp = []
        for i in range(len(player_times)-1):
            temp.append(player_times[i+1] - player_times[i])
        absolute_times.append(temp)

    return match(words, absolute_times)


    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"


#                [word_time, word, player_num]
    # return_list = [[]]
    # for k in range(len(get_all_times(match)) - 1):
    #     return_list.append([])
    
    return_list = [[] for _ in player_indices]

    for i in word_indices:
        least_time_record = [999, '', 0]
        for j in player_indices:
            if get_all_times(match)[j][i] < least_time_record[0]:
                least_time_record[0] = get_all_times(match)[j][i]       # time to type word
                least_time_record[1] = get_all_words(match)[i]          # the word typed
                least_time_record[2] = j                                # playerID
        # list_of_fastest_words.append(least_time_record[1])
        return_list[least_time_record[2]].append(least_time_record[1])
    return return_list
        

        

    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)