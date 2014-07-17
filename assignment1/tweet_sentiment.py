import sys
import json

# subroutine for calculating setiment scores for each tweets
def compute_score(text,scores):
    total = 0.0
    words = text.split()
    for word in words:
        if word in scores.keys():
            total = total + scores[word]
    return total

def main():
    sent_file = open(sys.argv[1]) # first argument of the function call is the sentiment file
    tweet_file = open(sys.argv[2]) # second argument of the function call is the tweets file
    
    # creating a dictionary for sentiment-word mapping
    scores = {} # initialize an empty dictionary to store sentiment scores for words
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        
    # creating a dictionary for tweet-sentiment_score mapping
    tweets_scores = {} # initialize an empty dictionary
    index = 0
    for line in tweet_file:
        index = index + 1
        tweet = json.loads(line)
        text = tweet.get("text")
        # calculating setiment score
        if text:
            text = text.encode("utf-8")
            tweets_scores[index] = compute_score(text,scores)
        else: tweets_scores[index] = 0.0
        
    # print out results
    for i in tweets_scores:
        print(str(tweets_scores[i]))

    
if __name__ == '__main__':
    main()