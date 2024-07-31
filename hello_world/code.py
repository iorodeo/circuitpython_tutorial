import time
from hello import say_hello

count = 0
while True:
    print(f'hello: {count=}')
    say_hello(count)
    count += 1
    time.sleep(0.1)




