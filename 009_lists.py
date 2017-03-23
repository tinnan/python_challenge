if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        inp = input().split(' ')
        cmd = inp[0]
        args = []
        if len(inp) > 1:
            for e in inp[1:]:
                try:
                    args.append(int(e))
                except ValueError:
                    continue

        if cmd == 'print':
            print(l)
        else:
            getattr(l, cmd)(*args)
