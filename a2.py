import csv

class Keyword:
    def __init__(self, name, txt):
        self.name = name
        self.txt = txt

class Tweet:
    def __init__(self, content):
        self.content = content


keywords = {}
with open('keywords_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        keywords[row[0]] = row[1]

tweets = []
with open('tweets.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tweets.append(Tweet(row['content']))

def loop(tweets, keywords):      #takes a list of tweet objects and keywords dictionary as inputs
    for tweet in tweets:		                                                #iterates each tweet in tweets list 
        newText = " ".join(keywords.get(word, word) for word in tweet.content.split())      #search and replace using hashmap             
        tweet.content = newText			                                            #replace tweet text with processed string
    return tweets 				                                                #after repeating for all tweets, return output

processed_tweets = loop(tweets, keywords)

# Print the processed tweets
for tweet in processed_tweets:
    print(tweet.content)