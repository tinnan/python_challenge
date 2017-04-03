"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

if __name__ == "__main__":
    M_size, M = int(input()), set(map(int, input().split()))
    N_size, N = int(input()), set(map(int, input().split()))
    S = M.difference(N)
    S.update(N.difference(M))
    for l in sorted(list(S)):
        print(l)
