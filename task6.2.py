import time

t = time.time()
sum = 0
for i in range(1000000):
    sum += i
secs = time.time() - t

with open(f"{time.strftime('%H.%M.%S_%d.%m.%Y')}.txt", "w") as f:
    f.write(str(secs))
