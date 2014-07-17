# compute the term frequency histogram of the livestream data 

# The frequency of a term can be calculated as [# of occurrences of the 
# term in all tweets]/[# of occurrences of all terms in all tweets]

# script will be run from the command line like this:
# $ python frequency.py <tweet_file>

import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    
    occurrence = {}
    
    # count number of occurrence for each word
    for line in tweet_file:
        tweet = json.loads(line)
        text = tweet.get("text")
        
        if text:
            text = text.encode("utf-8")
            words = text.split()
            
            for word in words:
                if word not in occurrence:
                    occurrence[word] = 1
                else:
                    occurrence[word] += 1
                    
                    
    total_occurrence = 0.0

    for i in occurrence:
        total_occurrence += int(occurrence[i])

    for i in occurrence:
        occurrence[i] = str(float(occurrence[i])/total_occurrence)
        print i,occurrence[i]


if __name__ == '__main__':
    main()