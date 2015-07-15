# example of program that calculates the total number of times each word has been tweeted.

import sys

def words_tweeted(inputfile,outputfile):
    f = open(inputfile, 'r')
    wordlist = dict()
    for line in f:
        words = list(line.split())
        for w in words:             # creating the dictionary with words as keys and their count as values
            if w not in wordlist:
                wordlist[w] = 1
            else:
                wordlist[w] = wordlist[w] + 1
        
    of = open(outputfile, 'w')     # writing the dictionary to the file to output
    total_keys = len(wordlist.keys())
    item_index = 0
    for key, value in sorted(wordlist.iteritems()):
        item_index += 1
        of.write(str(key.ljust(28)) + str(value))
        if item_index < total_keys:
             of.write('\n')
             
    f.close()
    of.close()
        
    
if __name__ == '__main__':
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    words_tweeted(inputfile,outputfile)