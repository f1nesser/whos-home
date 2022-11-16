import sys
import cv2

if len(sys.argv) != 2:
    print('usage: python3 camera.py <file name>')
    exit()

NAME = sys.argv[1]
COUNTER = 1

print('say cheese likeshit')
try:
    while True:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'{NAME}{COUNTER}.jpg', frame)
            print(COUNTER)
        COUNTER += 1
except KeyboardInterrupt:
    cap.release()
