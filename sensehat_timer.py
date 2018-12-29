import time

import show_in_sensehat
import logging

import config

profile = config.sleep_prof_list

# There is 8 leds in a row
SEGMENT = config.SEGMENT

def refresh_profile(profile_list):
    # print(profile_list)
    show_in_sensehat.profile(profile_list)


def refresh_progress_bar(pct, show_num):
    show_in_sensehat.show_number(show_num)
    show_in_sensehat.draw_progress_bar(pct)


def refresh_led(sleep_time):
    for i in range(SEGMENT):
        sleep_seg = sleep_time - i * sleep_time / SEGMENT
        show_num = int(sleep_seg - sleep_time / SEGMENT)
        pct = 1 - i / SEGMENT
        logging.info('Sleep {} {}'.format(show_num, pct))
        refresh_progress_bar(pct, show_num)
        # time.sleep(sleep_seg * 60)
        time.sleep(sleep_seg)


def run_profile(profile_list):
    for x in range(len(profile_list)):
        prf = profile_list[x]
        logging.info('Sleep profile {}, sleep {}'.format(x, prf))
        refresh_led(prf)
        profile_list[x] = False
        refresh_profile(profile_list)


if __name__ == '__main__':
    run_profile(profile)