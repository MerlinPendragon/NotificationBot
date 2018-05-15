import math
import time
from datetime import datetime

import pytz
import telegram

DAY_SECONDS = 24 * 60 * 60
HOUR_SECONDS = 60 * 60
MINUTE_SECONDS = 60


def previous_day_start(start_time):
    return math.floor((time.time() - start_time) / DAY_SECONDS) * DAY_SECONDS + start_time


def timestamp_to_str(t: int):
    timezone_local = pytz.FixedOffset(480)
    dt = pytz.utc.localize(datetime.utcfromtimestamp(t))
    return dt.astimezone(timezone_local).strftime("%Y-%m-%d %H:%M:%S")


def day_time_to_str(t: int):
    while t < 0:
        t += DAY_SECONDS
    return "{:02}:{:02}".format((t // HOUR_SECONDS + 8) % 24, (t % HOUR_SECONDS) // MINUTE_SECONDS)


def time_interval_to_remain(interval: int):
    if interval < 0:
        return "no time"
    s = []
    if interval > DAY_SECONDS:
        s.append("%d days" % (interval // DAY_SECONDS))
        interval = interval % DAY_SECONDS
    if interval > HOUR_SECONDS:
        s.append("%d hours" % (interval // HOUR_SECONDS))
        interval = interval % HOUR_SECONDS
    if interval > MINUTE_SECONDS:
        s.append("%d minutes" % (interval // MINUTE_SECONDS))
        interval = interval % MINUTE_SECONDS
    else:
        s.append("less than one minutes")
    return " ".join(s)


class BotPlugin:
    prefix = ""

    def __init__(self, bot: telegram.Bot):
        self.bot = bot

    def handle_command(self, user: telegram.User, chat: telegram.Chat, parameters: [str]):
        return ""

    def handle_callback(self, callback: telegram.CallbackQuery):
        return "", False
