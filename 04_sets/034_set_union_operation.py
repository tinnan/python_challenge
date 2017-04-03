"""
Example
>> s = set("Hacker")
>> print s.union("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>> print s.union(set(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>> print s.union(['R', 'a', 'n', 'k'])
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>> print s.union(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>> print s.union({"Rank":1})
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

Task
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed to only French and some have
subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
and the other set is subscribed to the French newspaper. The same student could be in both sets.
Your task is to find the total number of students who have subscribed to at least one newspaper.

"""

en_size, E = int(input()), set(map(int, input().split()))
fr_size, F = int(input()), set(map(int, input().split()))

U = E | F
print(len(U))
