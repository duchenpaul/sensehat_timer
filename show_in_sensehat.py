from sense_hat import SenseHat
import auto_orientation

import config
SEGMENT = config.SEGMENT


sense = SenseHat()
sense.low_light = True
sense.clear()
sense.rotation = auto_orientation.get_orientation()


COLOR_PROGRESS_BAR_OFF = 0, 0, 0
COLOR_PROGRESS_BAR_ON = 52, 163, 239  # light blue

COLOR_PROFILE_DONE = 105, 239, 52
COLOR_PROFILE_TODO = 201, 217, 191

COLOR_NUMBER = 239, 159, 52  # light orange

nums = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,  # 0 # 0
        0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,
        1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0,
        1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0,  # 9
        1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]  # T


def show_num(val, xd, yd, r, g, b):
    offset = val * 15
    for p in range(offset, offset + 15):
        if nums[p] == 1:
            xt = p % 3
            yt = (p - offset) // 3
            sense.set_pixel(xt + xd, yt + yd, r, g, b)


def show_number(val):
    r, g, b = COLOR_NUMBER
    abs_val = abs(val)
    tens = abs_val // 10
    units = abs_val % 10

    # clear digits
    for x, y in [(x,y) for x in range(8) for y in range(5)]:
        sense.set_pixel(x, y, 0, 0, 0)

    if (abs_val > 9):
        show_num(tens, 0, 0, r, g, b)
    show_num(units, 4, 0, r, g, b)
    if abs_val == 100:
        show_num(10, 3, 2, r, g, b)  # 'T' for ton = 100
    if val < 0:
        for i in range(0, 8):
            sense.set_pixel(i, 0, 0, 0, 128)


def profile(status_list):
    for i in range(len(status_list)):
        color = COLOR_PROFILE_DONE if status_list[i] else COLOR_PROFILE_TODO
        sense.set_pixel(i, 6, color)


def draw_progress_bar(percent):
    ledon = percent * 8
    # Set all lights off
    for i in range(SEGMENT):
        sense.set_pixel(i,7,COLOR_PROGRESS_BAR_OFF)
    for i in range(int(ledon)):
        sense.set_pixel(i,7,COLOR_PROGRESS_BAR_ON)


def clear_led():
    sense.clear()

if __name__ == '__main__':
    pass
