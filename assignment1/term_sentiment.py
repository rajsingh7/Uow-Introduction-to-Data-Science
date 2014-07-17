import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    # creating a dictionary for sentiment-word mapping
    scores = {} # initialize an empty dictionary to store sentiment scores for words
    for line in sent_file:
        term, score  = line.split("\t")  
        scores[term] = int(score)  # Convert # The file is tab-delimited. "\t" means "tab character"the score to an integer.
    
    new_scores = {}
    for line in tweet_file:
        tweet = json.loads(line)
        text = tweet.get("text")
        
        if text:
            text = text.encode("utf-8")
            words = text.split()
            sentiment = 0.0
            # calculate sentiment for each tweet
            for word in words:
                if word in scores:
                    sentiment += scores[word]
                    
            # using another dictionary to store sentiment mapping for words not 
            # in the "scores" dictionary

            # calculate sentiment for new words
            for word in words:
                if word not in scores:
                    new_score = 0.0
                    if word in new_scores:
                        new_score += new_scores[word]      
                    new_score += float(sentiment)/len(words)
                    if new_score == 0.0:
                        new_scores.pop(word,None)
                    else:
                        new_scores[word] = new_score
                        
    # print out sentiment scores for each new words
    for i in new_scores:
        print i, str(new_scores[i])

                


if __name__ == '__main__':
    main()
