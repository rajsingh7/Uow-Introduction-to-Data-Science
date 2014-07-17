import sys
import json
import re

def build_US_tweets_list(t_file, scores):
	state_tweet_dict = {}
	for line in t_file:
		if 'place' in line:
			temp = json.loads(line).get('place')
			if temp != None and temp.get('country_code').encode('utf-8') == 'US':
				text = json.loads(line).get('text').encode("utf-8")
				current_state = temp['full_name'].split(',')[1]
				if current_state in state_tweet_dict:
					state_tweet_dict[current_state] += get_tweet_sent(text, scores)
				else:
					state_tweet_dict[current_state] = get_tweet_sent(text, scores)
	return state_tweet_dict

# get_tweet_sent: string (dict: string int) -> int
# returns the sentiment of a tweet
def get_tweet_sent(tweet, s_list):
	running_sent = 0;
	tweet = re.split('[\. \, \? ! @ # \$ % ^ & \* ( ) \+ - ; : < > |]', tweet)
	for word in tweet:
		if word in s_list:
				running_sent += s_list[word]
	return running_sent

# print_happiest_state: (dict: string int) -> stdout
def print_happiest_state(US_tweet_dict):
	happiest_state = {'dummy' : -999999}
	for key, value in US_tweet_dict.items():
		if value > happiest_state.values()[0]:
			happiest_state = {key : value}
	print happiest_state.keys()[0]
#	print happiest_state.values()[0]

def main():
    sent_file = open(sys.argv[1]) # first argument of the function call is the sentiment file
    tweet_file = open(sys.argv[2]) # second argument of the function call is the tweets file
    
    # creating a dictionary for sentiment-word mapping
    scores = {} # initialize an empty dictionary to store sentiment scores for words
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    US_tweet_dict = build_US_tweets_list(tweet_file, scores)
    print_happiest_state(US_tweet_dict)

if __name__ == '__main__':
    main()