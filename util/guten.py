import nltk
from nltk.corpus import gutenberg
import re
import os

if not os.path.exists('books'):
    os.makedirs('books')

for fileid in gutenberg.fileids():
    f = open('books/' + fileid, "w")
    for words in gutenberg.sents(fileid):
        # skip short sentences; this avoids lines like "chaper 1", "book ix", and "actus primus"
        if len(words) < 4:
            continue
        
        # convert to a lower case string
        sent = ' '.join([w.lower() for w in words])
        
        # we only want verses of the bible, not book/chapter titles
        # so skip anything that doesn't have \d+ : \d+ at the beginning
        # and then remove the chapter:verse from the beginning of each line
        if fileid == 'bible-kjv.txt':
            if not re.match(r'\d+ : \d+', sent):
                continue
            else:
                sent = ' '.join([w.lower() for w in words[3:]])
        
        f.write(sent)
        f.write('\n')
    f.close()
    print(f'done with {fileid}')
    

