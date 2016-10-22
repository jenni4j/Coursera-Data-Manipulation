import sys
import json
import operator

scores = {}

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

state_sent = dict.fromkeys(states.keys(),0) # overall score per state
num_tweets = dict.fromkeys(states.keys(),0) # number of tweets in that state
avg_sent = dict.fromkeys(states.keys(),0) 

def word_sent():
    afinn_file = open(sys.argv[1])
    for line in afinn_file:
        term,score = line.split("\t")
        scores[term] = int(score)

def tweet_sent():
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        score = 0
        if 'text' in tweet:
            for word in tweet['text'].encode('utf-8').split():
                if word in scores:
                    score += scores[word]
        if 'user' in tweet and 'location' in tweet['user']:
            location = tweet['text'].encode('utf-8').split(', ')
            if len(location) == 2:
                for abbrev, name in states:
                    if location[1] == abbrev or location[1] == name:
                        state_sent[abbrev] += score
                        num_tweets[abbrev] += 1

    for state, state_score in state_sent:
        print num_tweets[state]
 #       avg_sent[state] = state_score/num_tweets[state]
        
    happiest = sorted(state_sent.items(), key = operator.itemgetter(1), reverse=True)[0]
    happy_state, state_sentiment = happiest
    print happy_state
    

def main():
    word_sent()
    tweet_sent()
    
if __name__ == '__main__':
    main()
