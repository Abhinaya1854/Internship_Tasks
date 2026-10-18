# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n = int(input())
english_subs = set(map(int, input().split()))
b = int(input())
french_subs = set(map(int, input().split()))
both_subs = english_subs.intersection(french_subs)
print(len(both_subs))