# are you root?

import cv2
import lgpio

motion_sensor = 14
counter = 1

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, motion_sensor)

while True:
    motion = lgpio.gpio_read(h, motion_sensor)
    if motion:
        print(f'caught in 4k {counter} times!')
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'{counter}.jpg', frame)
            counter += 1
        cap.release()
