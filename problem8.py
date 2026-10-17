# https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    country_set = set()
    for _ in range(n):
        country_set.add(input().strip())
    print(len(country_set))