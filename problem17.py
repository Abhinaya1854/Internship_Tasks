
# Problem: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Calculate the average using the boilerplate's variables
    query_scores = student_marks[query_name]
    average = sum(query_scores) / len(query_scores)
    
    # Print formatted to 2 decimal places
    print(f"{average:.2f}")
