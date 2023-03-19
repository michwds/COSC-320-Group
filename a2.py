
def loop(tweets, keywords):
    newText = ""			                                                    #initialise the “sublist”
    #map = {keys: keywords} - using "keywords" input instead 	                #populate hashmap with key value pairs
    for tweet in tweets:		                                                #iterates each tweet in tweets list 
        words = tweet.text.split()	                                            #delimits full text into a list of words
    newText = " ".join(keywords.get(word, word) for word in tweet.text.split())      #search and replace using hashmap             
    tweet.text = newText			                                            #replace tweet text with processed string
    return tweets 				                                                #after repeating for all tweets, return output