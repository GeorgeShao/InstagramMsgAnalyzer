import dateutil.parser as dp # ISO 8601 to Epoch time conversion library
from textblob import TextBlob # sentiment analysis library


def SentimentAnalysis(json_file: dict):
    '''
    Analyses entire JSON file of messages
    ''' 
    for i in json_file:
        for j in i['conversation']:
            time = int(dp.parse(j['created_at']).timestamp())
            sender = j['sender']
            if 'text' in j:
                analyzed_text = TextBlob(j['text'])
                print(f"[{time}] [{analyzed_text.sentiment.polarity}] {sender}: {j['text']}")
            else:
                print(f"[{time}] [N/A] {sender}: (HEART)")
        print('-'*10 + 'CONVERSATION_BREAK' + '-'*10)

