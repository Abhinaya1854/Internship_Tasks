
# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))

n = int(input())
earnings = 0

for _ in range(n):
    size, price = map(int, input().split())

    if sizes[size] > 0:
        earnings += price
        sizes[size] -= 1

print(earnings)
