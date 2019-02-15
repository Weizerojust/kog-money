# -*- coding: utf-8 -*-


import logging
import os
from time import sleep

# 屏幕分辨率
device_x, device_y = 2160, 1080

# 通关模式：1=重新挑战 -> 挑战界面，2=重新挑战-> 更换阵容
game_mode = 2

# 各步骤等待间隔
step_wait = [5, 13, 24, 3, 3]

# 刷金币次数
repeat_times = 100

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    os.system('adb shell input tap {} {}'.format(x, y))
    # base_x, base_y = 1920, 1080
    # real_x = int(x / base_x * device_x)
    # real_y = int(y / base_y * device_y)
    # os.system('adb shell input tap {} {}'.format(real_x, real_y))


def do_money_work():
    if game_mode == 1:
        logging.debug('#0 start the game')
        tap_screen(1826, 984)
        sleep(step_wait[0])

    logging.debug('#1 ready, go!!!')
    tap_screen(1826, 984)
    tap_screen(1600, 915)
    tap_screen(1826,915)
    sleep(step_wait[1])
    tap_screen(1826, 984)
    
    logging.debug('#2 please wait!')
    # tap_screen(1627, 936)

    for i in range(step_wait[2]):
        tap_screen(1870, 530)
        sleep(1)

    logging.debug('#3 do it again...\n')
    tap_screen(1826, 984)
    sleep(6)
    


if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('round #{}'.format(i + 1))
        do_money_work()
