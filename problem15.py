# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
n = int(input())
english_subs = set(map(int, input().split()))
b = int(input())
french_subs = set(map(int, input().split()))
english_only = english_subs.difference(french_subs)
print(len(english_only))