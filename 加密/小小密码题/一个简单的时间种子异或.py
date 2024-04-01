import random
import time

en = 881235169941718345882433419366
t = time.mktime(time.strptime("2022-12-10 10:30:50", "%Y-%m-%d %H:%M:%S"))

random.seed(t)
rand = random.randint(0,10**30)

flag = en^rand
print(flag)