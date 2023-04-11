import csv
import time
import glob
from random import choice

import matplotlib.pyplot as plt


class Keyword:
    def __init__(self, name, txt):
        self.name = name
        self.txt = txt

class Tweet:
    def __init__(self, content):
        self.content = content

def main():
    keywords = []
    with open('keywords_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            keywords.append(Keyword(row[0], row[1]))

    #Path to the folder containing the tweets
    tweets_folder_path = ''
    #Get all the files in the folder
    tweet_files = glob.glob(tweets_folder_path + '*.csv')
    tweets = []
    for file in tweet_files:
        with open(file, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                tweets.append(Tweet(row['content']))
    processed_tweets = []
    for tweet in tweets:
        processed_tweets.append(loop(tweet, keywords))



    # Print the processed tweets
    for tweet in processed_tweets:
        print(tweet.content)

    #print plot
    x, y = plot_runningTime(loop, tweets, keywords)
    print(x, y)
    plt.plot(x, y, color="red", label="Naive version")
    plt.xlabel("n tweets")
    plt.ylabel("Time(ms)")
    plt.legend()
    plt.axline((0, 0), (170, 0.025), linewidth=1, color='b')
    plt.show()


def getNtweets(tweets, number):        #gets a specified number of tweets as list
    nTweets = []
    for n in range(number):
        nTweets.append(tweets[n])
    return nTweets

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


#input tweets in a dataset,
#we increment the try tweet sentence numbers, and get time took to process for each different size set.
#we plot x value as the increasing number of tweets 1 to 170 (our whole dataset), and y value as time taken to process

def plot_runningTime(myfunction, tweets, keywords):
    x_values = []
    y_values=[]

    for x in range(10, len(tweets), 10):  #we want x tweets from tweets in our dataset: startN, endN, stepSize
        runtime = 0
        #for nTry in range(20):                            #this is for taking average time to took for refine the time data
        for tw in getNtweets(tweets,x):
                start_time = time.time()
                myfunction(tw, keywords)                  #time for processing 1 tweet
                end_time = time.time()
                runtime  += (end_time - start_time)
        #runtime = runtime/20                     #averaging the time to refine the time data
        x_values.append(x)                       #input size aka tweet number
        y_values.append(runtime)     #time taken to process
    return x_values,y_values


if __name__ =='__main__':
    main()