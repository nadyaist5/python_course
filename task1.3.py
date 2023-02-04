n = 128
sum = 0
i = 1

while (n > 0):
  sum = sum + n % 10
  n = n // 10
  i = i + 1

print(sum)