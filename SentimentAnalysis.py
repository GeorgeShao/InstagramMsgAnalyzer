import dateutil.parser as dp  # ISO 8601 to Epoch time conversion library
from textblob import TextBlob  # sentiment analysis library
import time as mytime


def SentimentAnalysis(json_file: list):
    start_time = mytime.time()
    num_msgs = 0
    user_data = dict()
    for i in json_file:
        for j in i['conversation']:
            # count num of msgs
            num_msgs += 1

            # convert ISO 8601 timestamp to Epoch timestamp
            time = int(dp.parse(j['created_at']).timestamp())
            
            # get sentiment analysis score
            print("Computing sentiment analysis scores..." + str(num_msgs))
            if 'text' in j and j['text']:
                if (2 - TextBlob(j['text']).sentiment.subjectivity) > 1:
                    analysis_score = TextBlob(j['text']).sentiment.polarity * (1 + TextBlob(j['text']).sentiment.polarity)
                else:
                    analysis_score = TextBlob(j['text']).sentiment.polarity * (1 + TextBlob(j['text']).sentiment.polarity) * (2 - TextBlob(j['text']).sentiment.subjectivity)
                if TextBlob(j['text']).sentiment.polarity < 0:
                    analysis_score = -analysis_score
                text = j['text']
            elif 'heart' in j and j['heart']:
                analysis_score = 1
                text = "(HEART)"
            elif 'story_share' in j and j['story_share']:
                analysis_score = 0
                text = "(STORY)"
            
            # save analysis data to user_data list
            if j['sender'] in user_data:
                user_data[j['sender']].append((text, time, analysis_score))
            else:
                user_data[j['sender']] = [(text, time, analysis_score)]
        
        # print('-'*10 + 'CONVERSATION_BREAK' + '-'*10)
    end_time = mytime.time()
    
    print(user_data["frankye8998"])
    print("Sentiment Analysis Runtime: " + str(int(end_time - start_time)) + "s")
    print("Sentiment Analysis Speed: " + str(int(num_msgs /     int(end_time - start_time))) + "msg/s")
    
    sum = 0
    for sender in user_data:
        for msg_tuple in user_data[sender]:
            sum += int(msg_tuple[2])
        print(sender + ": " + str(sum/num_msgs))