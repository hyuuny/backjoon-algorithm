result = list(map(int, str(input())))
result.sort(reverse=True)
for i in result:
  print(i, end="")