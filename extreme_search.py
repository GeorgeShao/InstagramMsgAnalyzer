import sys
import json
import dateutil.parser as dp  # ISO 8601 to Epoch time conversion library
import time as mytime # time library
from textblob import TextBlob  # sentiment analysis library


json_file = list(json.loads(open('messages.json').read()))
word = str(sys.stdin.readline()).rstrip()
print(f'Search Term: {word}')

start_time = mytime.time()

total_num_msgs = 0
results = []

for i in json_file:
    for j in i['conversation']:
        # count num of msgs
        total_num_msgs += 1

        # convert ISO 8601 timestamp to Epoch timestamp
        time_created = int(dp.parse(j['created_at']).timestamp())
        sender = j['sender']

        if 'text' in j and j['text'] != None:
            text = j['text']
        else:
            text = ""
        
        if 'media_url' in j:
            media_url = j['media_url']
        else:
            media_url = ""
        
        if 'likes' in j:
            likes = j['likes']
        else:
            likes = []
        
        if 'text' in j and j['text'] != None:
            if 'media_url' in j:
                if (sender == "george.gsg") and ((word.lower()) in (text.lower())):
                    results.append(str(f'{time_created}: {sender}: "{text}" | {media_url}'))
            else:
                if (sender == "george.gsg") and ((word.lower()) in (text.lower())):
                    results.append(str(f'{time_created}: {sender}: "{text}"'))

        print(f'Msg #: {total_num_msgs} | Time: {time_created} | Found: {len(results)}')

end_time = mytime.time()

for i in range(len(results)):
    print("")
    print(str(f"{i}: {results[i]}"))

print(f'Runtime: {round((end_time - start_time),2)}s')