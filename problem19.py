# https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        unique_chars = dict.fromkeys(substring)
        print("".join(unique_chars))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)