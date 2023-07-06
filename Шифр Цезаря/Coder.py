s = input()
p = s.split()
coded = ''
patched = 0
for i in range(len(p)):
    patched = 0
    for k in p[i]:
        if k.isalpha():
            patched += 1
    for j in p[i]:
        n = patched
        if j.isalpha():
            c = ('a', 'A')[j.isupper()]
            coded += chr(ord(c) + (ord(j) + n - ord(c)) % 26)
        else:
            coded += j
    coded += ' '
print(coded)
