"""
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country
stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.
"""
if __name__ == "__main__":
    S = set()
    for _ in range(int(input())):
        S.add(input())
    print(len(S))
