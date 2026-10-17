# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    word_counts = {}
    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1
    print(len(word_counts))
    print(*word_counts.values())