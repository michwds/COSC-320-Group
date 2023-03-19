
def loop(tweets, keywords):      #takes a list of tweet objects and keywords dictionary as inputs
    for tweet in tweets:		                                                #iterates each tweet in tweets list 
        newText = " ".join(keywords.get(word, word) for word in tweet.content.split())      #search and replace using hashmap             
        tweet.content = newText			                                            #replace tweet text with processed string
    return tweets 				                                                #after repeating for all tweets, return output