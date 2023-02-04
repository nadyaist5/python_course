s = 'Лёша на полке клопа нашёл'
s = ''.join(s.split(' '))
s = s.lower()
s_new = s[::-1]
count = 0

for i in range(len(s)):
  if s[i] == s_new[i]:
    count = count + 1
if count == len(s):
  print('True')
else:
  print('False')