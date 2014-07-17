import sys
import json

def count(tweet_line, counters):
	tweet = json.loads(tweet_line)

	# if tweet doesn't contain text, return zero
	if "entities" not in tweet:
		return
	entities = tweet["entities"]
	if "hashtags" not in entities:
		return

	hashtags = entities["hashtags"]

	# calc count for each word
	for hashtag in hashtags:
		word = hashtag["text"]
		new_count = 0
		if word in counters:
			new_count += counters[word]
		new_count += 1
		counters[word] = new_count

def main():
	tweet_file = open(sys.argv[1])

	# init counters
	counters = {}

	for tweet_line in tweet_file:
		count(tweet_line, counters)

	i = 0
	for term in sorted(counters, key=counters.get, reverse=True):
		i = i + 1
		print term, counters[term]
		if i >= 10:
			break


if __name__ == '__main__':
	main()
