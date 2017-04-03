if __name__ == '__main__':
    s = input()
    is_alnum = False
    is_al = False
    is_digit = False
    is_lower = False
    is_upper = False
    for str in s:
        if str.isalnum():
            is_alnum = True
        if str.isalpha():
            is_al = True
        if str.isdigit():
            is_digit = True
        if str.islower():
            is_lower = True
        if str.isupper():
            is_upper = True
    print(is_alnum)
    print(is_al)
    print(is_digit)
    print(is_lower)
    print(is_upper)
