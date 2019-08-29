import json # JSON file managing library
import dateutil.parser as dp # ISO 8601 to Epoch time conversion library
from textblob import TextBlob # sentiment analysis library
import time

# import pyperclip; print = pyperclip.copy

# sentiment analysis
# text readability
# more...?

ENABLE_SENTIMENT_ANALYSIS = False

json_file = json.loads(open('messages.json').read())

text_msgs = 0
heart_msgs = 0

for i in json_file:
    for j in i['conversation']:
        if 'text' in j:
            if ENABLE_SENTIMENT_ANALYSIS:
                analyzed_text = TextBlob(j['text'])
                print(f"[{int(dp.parse(j['created_at']).timestamp())}] [{analyzed_text.sentiment.polarity}] {j['sender']}: {j['text']}")
            else:
                print(f"[{int(dp.parse(j['created_at']).timestamp())}] [N/A] {j['sender']}: {j['text']}")
            text_msgs += 1
        else:
            print(f"[{int(dp.parse(j['created_at']).timestamp())}] [N/A] {j['sender']}: (HEART)") #TODO: sentiment analysis on heart based on previous msg(s) sent
            heart_msgs += 1
    print('-'*10 + 'CONVERSATION_BREAK' + '-'*10)

print("text_msgs: " + str(text_msgs))
print("heart_msgs: " + str(heart_msgs))
print("total_msgs: " + str(text_msgs + heart_msgs))