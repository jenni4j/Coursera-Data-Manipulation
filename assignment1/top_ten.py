import sys
import json
import operator

def top_ten():
    tweet_file = open(sys.argv[1])
    all_hashtags = {}

    for line in tweet_file:
        tweet = json.loads(line)

        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            hashtags = tweet['entities']['hashtags']
            for hashtag in hashtags:
                hashtag_text = hashtag['text'].encode('utf-8')
                if not hashtag_text in all_hashtags:
                    all_hashtags[hashtag_text] = 1
                else:
                    all_hashtags[hashtag_text] += 1
    sorted_hashtags = sorted(all_hashtags.items(), key = operator.itemgetter(1), reverse=True)
    tracker = 0
    for hashtag, hash_freq in sorted_hashtags:
        tracker += 1
        print hashtag + ' ' + str(hash_freq)
        if tracker == 10:
            break

def main():
    top_ten()
    
if __name__ == '__main__':
    main()
