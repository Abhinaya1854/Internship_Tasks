# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

    # Write your code here
from collections import Counter

def isValid(s):
    freqs = Counter(s).values()
    freq_map = Counter(freqs)
    
    if len(freq_map) == 1:
        return "YES"
        
    if len(freq_map) == 2:
        key1, key2 = freq_map.keys()
        

        if (freq_map[key1] == 1 and (key1 == 1 or key1 - 1 == key2)) or \
           (freq_map[key2] == 1 and (key2 == 1 or key2 - 1 == key1)):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
