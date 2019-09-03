import dateutil.parser as dp  # ISO 8601 to Epoch time conversion library
import time as mytime # time library
from textblob import TextBlob  # sentiment analysis library


def SentimentAnalysis(json_file: list):
    start_time = mytime.time()

    num_msgs = 0
    user_num_msgs = 0
    user_num_msgs_zero_rating = 0
    excluded = []
    sum = 0

    user_data = dict()

    # calculate sentiment analysis score for each message
    for i in json_file:
        for j in i['conversation']:
            # count num of msgs
            num_msgs += 1

            # convert ISO 8601 timestamp to Epoch timestamp
            time = int(dp.parse(j['created_at']).timestamp())

            # get sentiment analysis score
            print("Computing sentiment analysis scores..." + str(num_msgs))
            if 'text' in j and j['text']:
                analysis_score = TextBlob(j['text']).sentiment.polarity * (2 - TextBlob(j['text']).sentiment.subjectivity)
                text = j['text']
            elif 'heart' in j and j['heart']:
                analysis_score = 0.75
                text = "(HEART)"
            elif 'story_share' in j and j['story_share']:
                analysis_score = 0.4
                text = "(STORY)"

            # save analysis data to user_data list
            if j['sender'] in user_data:
                user_data[j['sender']].append((text, time, analysis_score))
            else:
                user_data[j['sender']] = [(text, time, analysis_score)]

    # calculate sentiment analysis score for each sender
    for sender in user_data:
        user_num_msgs = 0
        user_num_msgs_zero_rating = 0
        sum = 0
        for msg_tuple in user_data[sender]:
            # calculate sum of all the ratings
            user_num_msgs += 1
            if msg_tuple[2] == 0:
                user_num_msgs_zero_rating += 1
            sum += int(msg_tuple[2])
        if sum != 0 and (user_num_msgs - user_num_msgs_zero_rating) != 0 and ((user_num_msgs - user_num_msgs_zero_rating)/user_num_msgs) > 0.2 and (user_num_msgs - user_num_msgs_zero_rating) > 300 and not ("__deleted__" in sender):
            print(sender + ": " + str(round(sum/(user_num_msgs - user_num_msgs_zero_rating), 4)) + " ~ " + str(user_num_msgs) + " ~ " + str(user_num_msgs_zero_rating) + " ~ " + str(round((user_num_msgs - user_num_msgs_zero_rating)/user_num_msgs * 100)) + "%")
        else:
            excluded.append(sender)
    
    end_time = mytime.time()
    
    # output sentiment analysis results
    print("Sentiment Analysis Statistics: " + str(int(end_time - start_time)) + " s for " + str(num_msgs) + " msgs (" + str(int(num_msgs / int(end_time - start_time))) + " msg/s)")
    print("Excluded People: ", end = "")
    excluded_ppl = 0
    for person in excluded:
        print(person + " ", end = "")
        excluded_ppl += 1
    print("\n# of Excluded: " + str(excluded_ppl))