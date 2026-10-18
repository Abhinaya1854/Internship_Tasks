# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
import re
n = int(input())
pattern = r"^[789]\d{9}$"
for _ in range(n):
    string = input()
    if re.match(pattern, string):
        print("YES")
    else:
        print("NO")