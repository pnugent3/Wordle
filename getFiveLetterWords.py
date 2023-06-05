"""
Extract words of the specified length from the word list.
Takes a file with newline seperated words as input
"""

import os

#paths
base_d = os.path.dirname(__file__)+os.path.sep
print(base_d)
src_f = "twl06.txt"
out_f = "twl06FiveLetter.txt"
#how long are words we are extracting
searchLen = 5

#search src file and output 5 letter words to out file
with open(base_d+src_f,'r') as src:
    with open(base_d+out_f,'w') as out:
        line = ' '
        while len(line) > 0:
            line = src.readline()
            if len(line.rstrip()) != (searchLen):
                continue
            out.write(line)
