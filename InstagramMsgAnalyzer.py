import json # JSON file managing library

from SentimentAnalysis import SentimentAnalysis
# from ReadibilityAnalysis import ReadibilityAnalysis


# import pyperclip; print = pyperclip.copy

ENABLE_SENTIMENT_ANALYSIS = True
ENABLE_READIBILTY_ANALYSIS = False

json_file = json.loads(open('messages.json').read())

if ENABLE_SENTIMENT_ANALYSIS:
    SentimentAnalysis(json_file)

if ENABLE_READIBILTY_ANALYSIS:
    ReadibilityAnalysis(json_file)