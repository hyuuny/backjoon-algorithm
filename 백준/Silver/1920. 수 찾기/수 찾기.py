n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_search(value, start, end):
  if start > end : return False

  median = (start + end) // 2
  if n_list[median] > value:
    return binary_search(value, start, median-1)
  elif n_list[median] < value:
    return binary_search(value, median+1, end)
  else:
    return True

for item in m_list:
  if binary_search(item, 0, n-1):
    print(1)
  else:
    print(0)