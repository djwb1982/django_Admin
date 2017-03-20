import datetime
import time


def run(n):
    s = 0
    for i in range(0, n):
        for j in range(0, n):
            s += 1
    return s


def run_within_time(n, time_in_millisecond):
    s = 0

    start_time = long(time.time() * 1000)
    for i in range(0, n):
        for j in range(0, n):
            s += 1
        elapsed = long(time.time() * 1000) - start_time
        # 做完一部分任务后,判断是否超时
        if elapsed >= time_in_millisecond:
            s = -1
            break
    return s
