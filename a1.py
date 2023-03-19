
def loop(tweets, keywords):                 #tweets is a list of tweet objects, keywords is a list of key objects each with key-value pair
    newText = ""			                #initialise the “sublist”
    for tweet in tweets:			            #iterates each tweet in tweets list 
        words = tweet.content.split()	        #delimits full text into a list of words
        for idx, word in enumerate(words): 		#iterates each word in the list
            for key in keywords:	           #iterates each keyword in the abbreviation list
                if word == key.name: 	#checks to see if the word is a keyword
                    word = key.txt 	    #replaces abbreviation with full text
            if idx > 0:		                #add a space between words for the “sublist”
                newText += " "
            newText += word	                #construct the replacement text “sublist”
    tweet.content = newText			        #replace tweet text with processed string
    return tweets 				            #after repeating for all tweets, return output
