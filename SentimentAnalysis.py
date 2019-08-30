import dateutil.parser as dp # ISO 8601 to Epoch time conversion library
from textblob import TextBlob # sentiment analysis library


def SentimentAnalysis(json_file: dict):
    '''
    Analyses entire JSON file of messages
    ''' 
    for i in json_file:
        for j in i['conversation']:
            timestamp = int(dp.parse(j['created_at']).timestamp())
            if 'text' in j:
                if ENABLE_SENTIMENT_ANALYSIS:
                    analyzed_text = TextBlob(j['text'])
                    print(f"[{timestamp}] [{analyzed_text.sentiment.polarity}] {j['sender']}: {j['text']}")
                else:
                    print(f"[{timestamp}] [N/A] {j['sender']}: {j['text']}")
            else:
                print(f"[{timestamp}] [N/A] {j['sender']}: (HEART)")
        print('-'*10 + 'CONVERSATION_BREAK' + '-'*10)

