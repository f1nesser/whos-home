import lgpio

motion_sensor = 14

print(lgpio)

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h,motion_sensor)

while True:
    motion = lgpio.gpio_read(h, motion_sensor)
    if motion:
        print("hey there")
    else:
        print("---")

