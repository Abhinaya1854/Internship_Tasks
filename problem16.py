# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    shift = k % 26
    lower_shifted = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    upper_shifted = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    translation_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        lower_shifted + upper_shifted
    )
    
    return s.translate(translation_table)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()