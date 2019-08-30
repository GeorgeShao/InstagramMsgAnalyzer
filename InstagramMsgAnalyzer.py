import json # JSON file managing library

from SentimentAnalysis import SentimentAnalysis
# from ReadabilityAnalysis import ReadabilityAnalysis


# import pyperclip; print = pyperclip.copy

ENABLE_SENTIMENT_ANALYSIS = True
ENABLE_READABILTY_ANALYSIS = False

json_file = json.loads(open('messages.json').read())

if ENABLE_SENTIMENT_ANALYSIS:
    SentimentAnalysis(json_file)

if ENABLE_READABILTY_ANALYSIS:
    ReadabilityAnalysis(json_file)