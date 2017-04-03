if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [e[1] for e in students]
    scores.sort()
    first = scores[0]
    for s in scores:
        if s != first:
            second = s  # find second lowest score
            break
    names = [n[0] for n in filter(lambda e: e[1] == second, students)]
    names.sort()
    for n in names:
        print(n)
