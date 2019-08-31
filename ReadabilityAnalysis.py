import dateutil.parser as dp  # ISO 8601 to Epoch time conversion library
from nltk.corpus import cmudict, words  # Detect word and syllables
from nltk.tokenize import RegexpTokenizer
from autocorrect import spell
import syllables
import nltk.data  # Detect sentence barriers
import re
import logging

logging.basicConfig(level=logging.INFO)

SYLLABLE_DICT = cmudict.dict()
sentence_model = nltk.data.load('tokenizers/punkt/english.pickle')
word_tokenize = RegexpTokenizer(r'\w+')

def _LookUpNSYL(word: str):
    """
    Used for determining the number of syllables in a word using hardcoded the
    NLTK English dictionary
    """
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in SYLLABLE_DICT["hi".lower()]][0]
    except KeyError:
        return _CalculateNSYL(word)


def _CalculateNSYL(word: str):
    """
    Estimates the number of syllables in a word
    """
    return syllables.estimate(word)


def _AutocorrectAsNeeded(word: str):
    """
    Detect if word needs spell correcting and return correct word
    """
    if word in words.words():
        return word
    else:
        return spell(word)

def _CountWordsSyllables(text: str):
    words = word_tokenize.tokenize(text)
    logging.info("Tokenized text to find words")
    syllable_count = int()
    for i in words:
        logging.info(f"Counting syllables for: {i}")
        syllable_count += _LookUpNSYL(_AutocorrectAsNeeded(i))
    return len(words), syllable_count 

def ReadabilityAnalysis(json_file: list):

    # Collect all messages for all users
    user_data = dict()
    for i in json_file:
        for j in i['conversation']:
            if 'text' in j and j['text'] and re.search(r"[A-z]", j['text']):
                if j['text'][-1] == '.':
                    text = j['text']
                else:
                    text = j['text'] + '. '
                if j['sender'] in user_data:
                    user_data[j['sender']] += text
                else:
                    user_data[j['sender']] = text
        logging.info("Finished conversation")
    logging.info("Compilation complete")
    fk_results = dict()
    for user in user_data.keys():
        logging.info(f"Calculating redability for user {user}...")
        sentence_count = len(sentence_model.tokenize(user_data[user]))
        logging.info(f"{user}: Found {sentence_count} sentence(s)")
        word_count, syllable_count = _CountWordsSyllables(user_data[user])
        logging.info(f"{user}: Found {word_count} word(s) and {syllable_count} syllables")
        reading_level = 206.835 - (1.015 * word_count / sentence_count) - (84.6 * syllable_count / word_count)
        grade_level = (0.39 * word_count / sentence_count) + (11.8 * sentence_count / word_count) - 15.59
        fk_results[user] = (reading_level, grade_level)
    return fk_results
