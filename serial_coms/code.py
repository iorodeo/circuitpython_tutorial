import sys
import supervisor 

buffer = []
new_message = False

while True:

    while supervisor.runtime.serial_bytes_available:
        byte = sys.stdin.read(1)
        if byte != '\n':
            buffer.append(byte)
        else:
            message = ''.join(buffer)
            buffer = []
            new_message = True
            break

    if new_message:
        print(f'received: {len(message)} bytes')
        print(f'message:  {message}')
        print()
        buffer = []
        new_message = False
        



