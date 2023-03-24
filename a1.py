import csv

class Keyword:
    def __init__(self, name, txt):
        self.name = name
        self.txt = txt

class Tweet:
    def __init__(self, content):
        self.content = content


keywords = []
with open('keywords_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        keywords.append(Keyword(row[0], row[1]))



tweets = []
with open('tweets.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tweets.append(Tweet(row['content']))


def loop(tweet, keywords):                 #tweets is a list of tweet objects, keywords is a list of key objects each with key-value pair
    newText = ""			                #initialise the “sublist”
    words = tweet.content.split()	        #delimits full text into a list of words
    for idx, word in enumerate(words): 		#iterates each word in the list
        for key in keywords:	           #iterates each keyword in the abbreviation list
            if word == key.name: 	#checks to see if the word is a keyword
                word = key.txt 	    #replaces abbreviation with full text
        if idx > 0:		                #add a space between words for the “sublist”
            newText += " "
        newText += word	                #construct the replacement text “sublist”
    tweet.content = newText			        #replace tweet text with processed string
    newText=""
    return tweet 				            #after repeating for all tweets, return output

processed_tweets = []
for tweet in tweets:
    processed_tweets.append(loop(tweet, keywords))

# Print the processed tweets
for tweet in processed_tweets:
    print(tweet.content)