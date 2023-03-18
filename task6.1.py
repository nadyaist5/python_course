import time

print("Введите число")
number = float(input())

while number >= 0:
    time.sleep(number)
    print("Введите число")
    number = float(input())
