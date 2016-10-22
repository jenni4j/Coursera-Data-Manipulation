import sys
import json

scores = {}
new_words = {}

def word_sent():
    afinn_file = open(sys.argv[1])
    for line in afinn_file:
        term,score = line.split("\t")
        scores[term] = int(score)

def find_unknown():
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweets = json.loads(line)
        score = 0
        if 'text' in tweets:
            for word in tweets['text'].encode('utf-8').split():
                if word in scores:
                    score += scores[word]
                elif  word in new_words:
                    new_words[word] += score
                else:
                    new_words[word] = score
                    

def print_unknown():
    for word, score in new_words.iteritems():
        print word, score

def main():
    word_sent()
    find_unknown()
    print_unknown()

if __name__ == '__main__':
    main()
