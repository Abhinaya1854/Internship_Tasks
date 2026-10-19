# https://www.hackerrank.com/challenges/funny-string/problem
import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    n = len(s)
    for i in range(n - 1):
        
        left_diff = abs(ord(s[i]) - ord(s[i + 1]))
        right_diff = abs(ord(s[n - 1 - i]) - ord(s[n - 2 - i]))
        
        if left_diff != right_diff:
            return "Not Funny"
            
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
