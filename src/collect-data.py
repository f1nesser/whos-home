"""When motion is detected, save a short animation"""
from datetime import datetime
import time
import cv2
import lgpio
import imageio

MOTION_SENSOR = 14
ANIM_LEN = 7

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, MOTION_SENSOR)

while True:
    motion = lgpio.gpio_read(h, MOTION_SENSOR)
    if motion:
        frames = []
        cur_datetime = datetime.now().strftime('%b,%d,%a,%H:%M:%S')
        print('capturing')
        for i in range(ANIM_LEN):
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
            cap.release()
        print(f'saving {cur_datetime}.gif')
        with imageio.get_writer(f'../img/{cur_datetime}.gif', mode = 'I') as writer:
            for brg_frame in frames:
                rgb_frame = brg_frame[:, :, ::-1]
                writer.append_data(rgb_frame)
        print('saved')
        time.sleep(3)
        print('ready')
