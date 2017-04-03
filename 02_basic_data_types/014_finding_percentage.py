if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_avgs = {}
    for name in student_marks:
        marks = student_marks[name]
        student_avgs[name] = '{:.2f}'.format(sum(marks) / len(marks))

    print(student_avgs[query_name])
