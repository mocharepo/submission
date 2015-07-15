# submission
## Solution to the Insight Data Engineering - Coding Challenge
This repository is submitted as a solution the coding challenge given in https://github.com/InsightDataScience/cc-example. 

## Contents
The repository contains a run file and three directories for source code, inout and output files. 

## File to run
run.sh is the file to run the program. It has two lines to execute the two features with corresponding arguments.

## Source code files
The directory contains two files - words_tweeted.py and median_unique.py

words_tweeted.py takes two arguments - path to input tweet text file and path to output file. It is written using the sys library. It writes to the output file the words and their count in the tweets saved in the input text file. The words are arranged in an order according to ASCII.

median_unique.py takes two arguments - path to input tweet text file and path to output file. It is written using sys and bumpy libraries. It reads the text file with tweets and gives the median of number of unique words in each line. As new tweet arrives, the program updates the median and writes in the new line of the output file. 

## Input file
The program takes the text file with tweets as input and reads the lines. 

## Output files
Each feature outputs its results into one file each. ft1.txt has the list of words with their count. ft2.txt has the median of number of unique words in each tweet.

## Dependencies
The program is written in Unix environment and uses sys and numpy libraries.