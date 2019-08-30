import dateutil.parser as dp # ISO 8601 to Epoch time conversion library
from nltk.corpus import cmudict

d = cmudict.dict()
def nsyl(word):

    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]  


def ReadabilityAnalysis(json_file: dict):
    pass