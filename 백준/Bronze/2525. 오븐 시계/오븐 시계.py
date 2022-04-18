while True:
  A, B = map(int, input().split())
  C = int(input())

  if 23 < A or 0 > A: continue
  if 59 < B or 0 > B: continue
  if 1000 < C or 0 > C: continue
  
  A += C // 60
  B += C % 60

  if B >= 60:
    A += 1
    B -= 60
  if A >= 24:
    A -= 24
  
  print(A, B)
  break
  