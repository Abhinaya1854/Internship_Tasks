# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    m_size = int(input())
    m_set = set(map(int, input().split()))
    n_size = int(input())
    n_set = set(map(int, input().split()))
    sym_diff = sorted(m_set.symmetric_difference(n_set))
    for num in sym_diff:
        print(num)
