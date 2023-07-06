s = input()
for j in range(1, 26):
    print(f'{j}:')
    for i in s:
        if i.isalpha():
            c = ('a', 'A')[i.isupper()]
            print(chr(ord(c) + (ord(i) + j - ord(c)) % 26), end='')
        else:
            print(i, end='')
    print()
