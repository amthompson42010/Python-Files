################################################
#
#  Project 4    April 11, 2014
#  Huffman Codes
#
#  Alexander M. Thompson
#
#  File: HuffCount.py
#
################################################

from collections import * #imports all that is needed to count the characters in the file and to order the dictionary

def readFile():
    with open("source.txt", 'rt') as f: #opens the file as read only and sets it to f
        characters = []
        for line in f:
            for c in line:
                characters.append(ord(c)) #breaks the file into characters and appends it to the empty array defined above and also instead of the character itself it append the ordance of that character
        counts = Counter(characters) #Counts the number of occurances of each character
    with open("counts.txt", 'w') as f: # opens the output file as write only
        order = OrderedDict(sorted(counts.items(), key=lambda t: t[0])) #sorts the dictionary
        for key, value in order.items():
            f.write("%s %s \n" % (key, value)) # writes the output to the given file above

def readFile2():
    with open("source.txt", 'rt') as f:
        characters = []
        for line in f:
            for c in line:
                characters.append(c)
        return characters

def compress(data):
    
def main():
    
