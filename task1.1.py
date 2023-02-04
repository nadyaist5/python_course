def season(n):
    if (n == 12) or (n == 1) or (n == 2):
        return 'winter'
    if (n == 3) or (n == 4) or (n == 5):
        return 'spring'
    if (n == 6) or (n == 7) or (n == 8):
        return 'summer'
    if (n == 9) or (n == 10) or (n == 11):
        return 'autumn'

print(season(7))
print ('\n:)')