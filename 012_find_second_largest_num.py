if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    first = arr[0]
    for i in arr[1:]:
        if i != first:
            second = i
            break
    print(second)
