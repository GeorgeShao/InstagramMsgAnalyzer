import json # JSON file managing library
import dateutil.parser as dp # ISO 8601 to Epoch time conversion library
from textblob import TextBlob # sentiment analysis library

# import pyperclip; print = pyperclip.copy

# sentiment analysis
# text readability
# more...?

a = json.loads(open('messages.json').read())

for i in a:
    for j in i['conversation']:
        if 'text' in j:
            text_to_be_analyzed = j['text']
            blob = TextBlob(text_to_be_analyzed)
            print(f"[{dp.parse(j['created_at']).timestamp()}] {blob.sentiment.polarity} {j['sender']}: {j['text']}")
        else:
            print(f"[{dp.parse(j['created_at']).timestamp()}] {j['sender']}: (HEART)")
        
    print('-'*10+'CONVERSATION-BREAK'+'-'*10)