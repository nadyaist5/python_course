import time
import os

t = time.time()
sum = 0
for i in range(1000000):
    sum += i
secs = time.time() - t

with open("f.txt", "w") as f:
    f.write(str(secs))
os.rename("f.txt", f"{time.strftime('%H.%M.%S_%d.%m.%Y')}.txt")