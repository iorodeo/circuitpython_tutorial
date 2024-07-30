# code.py
# -----------------------------------
import time

filename = 'data.txt'

print(f'writing: {filename}')
with open(filename, 'w') as f:
    for i in range(100):
        f.write(f'{i=}\n')
print('done')

count = 0
while True:
    print(f'hello, {count=}')
    count += 1
    time.sleep(1.0)



