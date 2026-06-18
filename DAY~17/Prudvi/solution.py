lst = [4, 200, 7, 1, 5];
inf = []

for i in range(len(lst)):
  l_count = 0
  r_count = 0
  for j in range(len(lst)):
    if j < i:
      if(lst[j] < lst[i]):
        l_count += 1
    elif j > i:
      if(lst[j] > lst[i]):
        r_count += 1
  print(l_count, r_count)
  inf.append(l_count - r_count)
print(inf)