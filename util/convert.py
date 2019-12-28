"""
Convert spam and ham from files into tab-separated values files .tsv
This makes it easier to distribute training files to students,
and matches up better with how Kaggle distributes training data.
"""

import os
import glob

def convert(path, tag):
    lines = []
    for filename in glob.glob(path):
        msg = []
        for line in [line.rstrip().lower() for line in open(filename, errors='ignore').readlines()[1:]]:
            for word in line.split():
                msg.append(word)
        lines.append(f"{tag}\t{' '.join(msg)}")
    return '\n'.join(lines)


f = open('enron.txt', 'w')

f.write(convert('docs/enron1/spam/*', 'spam') + '\n')
f.write(convert('docs/enron2/spam/*', 'spam') + '\n')
f.write(convert('docs/enron1/ham/*', 'ham') + '\n')
f.write(convert('docs/enron2/ham/*', 'ham') + '\n')

# f.write(convert('docs/basictest/spam/*', 'spam'))
# f.write(convert('docs/basictest/ham/*', 'ham'))

f.close()