"""
Game Rules
----------
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
----------
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Task
----------
Determine the winner of the game and their score.
"""
vowels = ['A', 'E', 'I', 'O', 'U']


def minion_game(string=''):
    stuart, kevin = 0, 0
    size = len(string)
    for i in range(size):
        if string[i] not in vowels:  # Stuart
            stuart += size-i
        else:  # Kevin
            kevin += size-i
    if stuart == kevin:
        print('Draw')
    elif stuart > kevin:
        print('Stuart {:d}'.format(stuart))
    else:
        print('Kevin {:d}'.format(kevin))
    return [stuart, kevin]


if __name__ == '__main__':
    s = input()
    print('Stuart={}  Kevin={}'.format(*minion_game(s)))
