import random
import time
foo = ['a', 'b', 'c', 'd', 'e']
for i in range(100000):
    print(random.choice(foo))
    time.sleep(0.3)