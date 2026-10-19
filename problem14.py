# https://www.hackerrank.com/challenges/anagram/problem
import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    if n % 2 != 0:
        return -1
        
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Map frequency of characters in the first half
    char_counts = {}
    for char in s1:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Subtract frequency for characters present in the second half
    changes = 0
    for char in s2:
        if char in char_counts and char_counts[char] > 0:
            char_counts[char] -= 1
        else:
            changes += 1
            
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
