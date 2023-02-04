list = []

def unique(list):
  count = 0
  for i in range(len(list)):
    for j in range(i+1, len(list)):
      if list[i] == list[j]:
        count = count + 1
  if count > 0:
    return True
  else:
    return False

print(unique([1, 2, 3, 1, 4]))