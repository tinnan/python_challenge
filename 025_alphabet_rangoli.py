"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Ex. Size = 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
# unicode base
base = 96  # 97 is 'a' in unicode


def print_rangoli(size):
    line_size = 4*size - 3
    plist = []
    for i in range(size):  # i as running 0, 1, 2, 3, ... (also number of character on each line)
        main_char = size - i
        num, char_count = [], 2*i+1
        mid = char_count // 2
        for x in range(char_count):
            # turn 0, 1, 2, 3, 4 -> 2, 1, 0, 1, 2
            if x <= mid:  # left side
                num.append(mid - x + main_char + base)
            else:  # right side
                num.append(main_char + x - mid + base)

        plist.append(('{:c}-'*i + '{:c}' + '-{:c}'*i).format(*num))
    for p in plist:
        print(p.center(line_size, '-'))  # print top half
    for p in reversed(plist[:len(plist)-1]):  # print bottom half as reversed list of the top half (minus the last line)
        print(p.center(line_size, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
