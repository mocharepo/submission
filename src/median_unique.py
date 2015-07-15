# example of program that calculates the median number of unique words per tweet.

import sys
import numpy as np

def median_unique(inputfile,outputfile):
    f = open(inputfile, 'r')
    of = open(outputfile, 'w')
    lines_in_file = f.readlines()
    number_unique = []          # initializing a list to store the numer of unique words in each tweet
    total_lines = len(lines_in_file)
    line_number = 0
    for line in lines_in_file:
        line_number += 1
        uniquewords = set(list(line.split()))   # creating a list of unique words in each tweet
        number_unique.append(len(uniquewords))
        uniquemedian = np.median(number_unique)  # median of the number of unique words till the last tweet
        of.write('%.2f' %uniquemedian)
        if line_number < total_lines:
            of.write('\n')
    
    f.close()
    of.close()

if __name__ == '__main__':
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    median_unique(inputfile,outputfile)