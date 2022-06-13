n = str(input())
count = 1

for i in n:
  if count == 10:
    print(i, end= "\n")
    count = 1
  else:
    print(i, end= "")
    count += 1