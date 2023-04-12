import csv
import glob
import time
import matplotlib.pyplot as plt

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

    #Path to the folder containing the tweets
    tweets_folder_path = "COSC320_Project_Dataset/"
    #Get all the files in the folder
    files = glob.glob(tweets_folder_path + '*.csv')
    tweets = []

    for file in files:
     with open(file, mode='r', encoding='utf-8') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      try:
       for row in csv_reader:
          tweets.append(Tweet(row['content']))
      except:
          print("error detected")
          continue


   
    plot_runtime(a1, a2, tweets, keywords1, keywords2, 5)
   




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

def printT(processed_tweets):        # Print the processed tweets
    for i, tweet in enumerate(processed_tweets):
        print(i)
        print(tweet.content)

def plot_runtime(myfunction1, myfunction2, tweets, keywords1, keywords2, threshold):

    print("plot function execution started...")
    x_values1 = []
    y_values1 = []
    x_values2 = []
    y_values2 = []
    numOfTw1 =0
    numOfTw2 =0
    counttime1 = 0
    counttime2 = 0
    runtime1 = 0
    runtime2 = 0

    for tw in tweets:

        #"function execution" block

        start_time1 = time.time()
        myfunction1(tw, keywords1)  # time for processing 1 tweet
        end_time1 = time.time()

        start_time2 = time.time()
        myfunction2(tw, keywords2)  # time for processing 1 tweet
        end_time2 = time.time()

        #"count tweet number processed and runtime" block
        numOfTw1 += 1
        numOfTw2 += 1
        counttime1 += (end_time1 - start_time1) #this is used for checking time threshhold (accumulated time of function run)
        counttime2 += (end_time2 - start_time2)

        #"intial data" block
        if counttime1 <= threshold and runtime1 == 0:
            y_values1.append(counttime1)
            x_values1.append(numOfTw1)
        if counttime2 <= threshold and runtime2 == 0:
            y_values2.append(counttime2)
            x_values2.append(numOfTw2)

        #"check thresholding" block
        if(counttime2 > threshold):
            runtime2 += counttime2
            y_values2.append(runtime2)
            x_values2.append(numOfTw2)
            counttime2 = 0

        if(counttime1 > threshold):
            runtime1 += counttime1 #runtime is stored in accumulated manner. ex) 5sec, 10sec, ....
            y_values1.append(runtime1)
            x_values1.append(numOfTw1)
            counttime1 = 0        #since counttime is just for threshold checking, we need to initialize after we successfully store the data. Then another round starts.

    #"the last discarded data" block
    if(runtime1 > 0):
        y_values1.append(runtime1)
        x_values1.append(numOfTw1)
    if(runtime2 > 0):
        y_values2.append(runtime2)
        x_values2.append(numOfTw2)

    #"plot" block
    plt.plot(x_values1, y_values1, color="red", label="Naive version")
    plt.plot(x_values2, y_values2, color="b", label = "Improved version")
    plt.ylabel("Processed Time (seconds)")
    plt.xlabel("Number of Tweets Processed (millions)")
    plt.legend()
    plt.show()

if __name__ =='__main__':
    main()
