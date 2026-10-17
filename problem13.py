# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique_scores = sorted(set(score for name, score in students))
    second_lowest_score = unique_scores[1]
    result_names = sorted([name for name, score in students if score == second_lowest_score])
    for name in result_names:
        print(name)