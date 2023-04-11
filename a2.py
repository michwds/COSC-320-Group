import csv

class Tweet:
    def __init__(self, content):
        self.content = content

class Keyword:
    def __init__(self, name, txt):
        self.name = name
        self.txt = txt
def main():
    keywords1 = []
    with open('keywords_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            keywords1.append(Keyword(row[0], row[1]))

    keywords2 = {}
    with open('keywords_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            keywords2[row[0]] = row[1]

    tweets = []
    with open('tweets.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tweets.append(Tweet(row['content']))
    
    processed_tweets1 = process(a1, tweets, keywords1)

    processed_tweets2 = process(a2, tweets, keywords2)

def a2(tweet, keywords):      #takes a list of tweet objects and keywords dictionary as inputs
    newText = " ".join(keywords.get(word, word) for word in tweet.content.split())      #search and replace using hashmap             
    tweet.content = newText			                                            #replace tweet text with processed string
    return tweet 				                                                #after repeating for all tweets, return output

def a1(tweet, keywords):                 #tweets is a list of tweet objects, keywords is a list of key objects each with key-value pair
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

def process(loop, tweets, keywords):
    for tweet in tweets:
        loop(tweet, keywords)
    return tweets

def print(processed_tweets):        # Print the processed tweets
    for i, tweet in enumerate(processed_tweets):
        print(i)
        print(tweet.content)

if __name__ =='__main__':
    main()