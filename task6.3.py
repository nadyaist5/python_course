import time

date = input()
birth = time.strptime(date, '%d.%m.%Y')
now = time.localtime()

print((time.mktime(now) - time.mktime(birth)) // 86400)