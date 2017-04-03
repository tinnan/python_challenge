"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing  integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i is a member of A, you add 1 to your happiness.
If i is a member of B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
"""

if __name__ == "__main__":
    array_size, set_size = list(map(int, input().split()))
    n = list(map(int, input().split()))
    A, B = set(map(int, input().split())), set(map(int, input().split()))
    happiness = 0
    for i in n:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)
