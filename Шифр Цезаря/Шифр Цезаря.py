n, s = int(input()), input()
for i in s:
    if i.isalpha():
        c = ('a', 'A')[i.isupper()]
        print(chr(ord(c) + (ord(i) + n - ord(c)) % 26), end='')
    else:
        print(i, end='')