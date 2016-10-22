import sys
import json

scores = {}

def word_sent():
    afinn_file = open(sys.argv[1])
    for line in afinn_file:
        term,score = line.split("\t")
        scores[term] = int(score)

def tweet_sent():
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweets = json.loads(line)
        score = 0
        if 'text' in tweets:
            for word in tweets['text'].encode('utf-8').split():
                if word in scores:
                    score += scores[word]
        print score

def main():
    word_sent()
    tweet_sent()
    
if __name__ == '__main__':
    main()
