import json # JSON file managing library
import dateutil.parser as dp # ISO 8601 to Epoch time conversion library
from textblob import TextBlob # sentiment analysis library
import time

# import pyperclip; print = pyperclip.copy

# sentiment analysis
# text readability
# more...?

ENABLE_SENTIMENT_ANALYSIS = True

json_file = json.loads(open('messages.json').read())

num_text_msgs = 0
num_heart_msgs = 0

for i in json_file:
    for j in i['conversation']:
        if 'text' in j:
            if ENABLE_SENTIMENT_ANALYSIS:
                analyzed_text = TextBlob(j['text'])
                print(f"[{int(dp.parse(j['created_at']).timestamp())}] [{analyzed_text.sentiment.polarity}] {j['sender']}: {j['text']}")
            else:
                print(f"[{int(dp.parse(j['created_at']).timestamp())}] [N/A] {j['sender']}: {j['text']}")
            num_text_msgs += 1
        else:
            if ENABLE_SENTIMENT_ANALYSIS:
                analyzed_text = TextBlob(json_file[i]['conversation'][j-1]['text']) #INPROG: sentiment analysis on heart based on previous msg(s) sent
                print(f"[{int(dp.parse(j['created_at']).timestamp())}] [{analyzed_text.sentiment.polarity}] {j['sender']}: (HEART)")
            else:
                print(f"[{int(dp.parse(j['created_at']).timestamp())}] [N/A] {j['sender']}: (HEART)")
            num_heart_msgs += 1
    print('-'*10 + 'CONVERSATION_BREAK' + '-'*10)

print("text_msgs: " + str(num_text_msgs))
print("heart_msgs: " + str(num_heart_msgs))
print("total_msgs: " + str(num_text_msgs + num_heart_msgs))