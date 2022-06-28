s = input()
print(s[:s.index('(')].count('@'))
print(s[s.index(')') + 1:].count('@'))