# https://www.hackerrank.com/challenges/py-set-union/problem
n = int(input())
english_subs = set(map(int, input().split()))
b = int(input())
french_subs = set(map(int, input().split()))
total_unique_students = english_subs.union(french_subs)
print(len(total_unique_students))