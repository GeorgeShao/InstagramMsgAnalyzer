import dateutil.parser as dp  # ISO 8601 to Epoch time conversion library
from nltk.corpus import cmudict, words  # Detect word and syllables
from autocorrect import spell
import syllables
import nltk.data  # Detect sentence barriers

d = cmudict.dict()
sentence_model = nltk.data.load('tokenizers/punkt/english.pickle')


def _LookUpNS(word: str):
    """
    Used for determining the number of syllables in a word using hardcoded the
    NLTK English dictionary
    """
    word = _AutocorrectAsNeeded(word)
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
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


def ReadabilityAnalysis(json_file: dict):
    user_data = dict()
    for i in json_file:
        for j in i['conversation']:
            if 'text' in j:
                if j['text'][-1] == '.':
                    text = j['text']
                else:
                    text = j['text'] + '.'
                if j['sender'] in user_data:
                    user_data[j['sender']] += message
                else:
                    user_data[j['sender']] = message
                return user_data  # XXX testing only
