import sys
import json

def freq():
    tweet_file = open(sys.argv[1])
    frequencies = {}
    total = 0
    for line in tweet_file:
        tweets = json.loads(line)
        
        if 'text' in tweets:
            for word in tweets['text'].encode('utf-8').split():
                total += 1
                if not word in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
                    
    for word, word_count in frequencies.items():
        print word, word_count/total

def main():
    freq()
    
if __name__ == '__main__':
    main()
