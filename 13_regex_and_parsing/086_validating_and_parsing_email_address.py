"""
A valid email address meets the following criteria:

- It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
- The username starts with an English alphabetical character, and any subsequent characters consist of one or more of
the following: alphanumeric characters, -,., and _.
- The domain and extension contain only English alphabetical characters.
- The extension is 1, 2, or 3 characters in length.

Given n pairs of names and email addresses as input, print each name and email address pair having a
valid email address on a new line.

Hint: Try using Email.utils() to complete this challenge. For example, this code:
"""
import re
import email.utils as mu

mail = re.compile(r'^[a-z][a-z0-9-._]*@[a-z]+\.[a-z]{1,3}$')

for _ in range(int(input())):
    a = mu.parseaddr(input())
    if bool(mail.match(a[1])):
        print(mu.formataddr(a))
