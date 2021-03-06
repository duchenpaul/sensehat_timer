import logging_manager
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
        logging.info('Sleep {} {}'.format(sleep_time / SEGMENT, show_num))
        refresh_progress_bar(pct, show_num)
        time.sleep(sleep_time / SEGMENT * 60)
        # time.sleep(sleep_time / SEGMENT)


@logging_manager.logging_to_file
def run_profile(profile_list):
    refresh_profile([True, True, True, True])
    for x in range(len(profile_list)):
        prf = profile_list[x]
        logging.info('Sleep profile {}, sleep {}'.format(x, prf))
        refresh_led(prf)
        profile_list[x] = False
        refresh_profile(profile_list)


if __name__ == '__main__':
    try:
        show_in_sensehat.clear_led()
        run_profile(profile)
    except Exception as e:
        logging.exception(e)
    finally:
        show_in_sensehat.clear_led()
    