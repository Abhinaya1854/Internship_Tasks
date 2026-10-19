# https://www.hackerrank.com/challenges/separate-the-numbers/problem
import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#
    # Write your code here
def separateNumbers(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        first_str = s[:length]
        if first_str[0] == '0':
            continue
            
        current_val = int(first_str)
        first_num = current_val
        idx = length
        valid = True
        
        while idx < n:
            next_val = current_val + 1
            next_str = str(next_val)
            next_len = len(next_str)
            if s[idx:idx + next_len] != next_str:
                valid = False
                break
                
            idx += next_len
            current_val = next_val
            
        if valid:
            print(f"YES {first_num}")
            return
            
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
