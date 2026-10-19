# https://www.hackerrank.com/challenges/game-of-thrones/problem
import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    bitmask = 0
    for char in s:
        bitmask ^= (1 << (ord(char) - ord('a')))
    if bitmask == 0 or (bitmask & (bitmask - 1)) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
