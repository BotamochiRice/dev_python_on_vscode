# -*- code:utf-8 -*-
from pytz import timezone
from datetime import datetime
from localtime.base import get_current_local_time


TZ_ASIA_TOKYO = timezone("Asia/Tokyo")
DATE_FORMAT = "%Y年%m月%d日"
TIME_FORMAT = "%H時%M分%S秒"
WEEKDAYS = ['月', '火', '水', '木', '金', '土', '日']


def get_curret_jst() -> datetime:
    """This returns current local time in JST(Japan Standard Time).

    Returns:
        datetime: current localtime in JST
    """
    return get_current_local_time(TZ_ASIA_TOKYO)


def get_japanese_weekday(weekday_index: int, long_format: bool = False) -> str:
    """This returns weekday in the Japanese weekday format.

    Args:
        weekday_index (int): datetime.weekday(): int
        long_format (bool, optional): returns weekday with "曜日" if True.
            returns weekday in one letter format if False. Defaults to False.

    Returns:
        str: weekday in the Japanese weekday format.
    """
    if weekday_index not in range(7):
        return ""

    ret = WEEKDAYS[weekday_index]
    if long_format:
        ret += "曜日"

    return ret


if __name__ == "__main__":
    jst_now = get_curret_jst()
    print(jst_now)  # 2020-11-07 11:16:38.959435+09:00
    print(jst_now.strftime(DATE_FORMAT))  # 2020年11月07日
    print(jst_now.strftime(TIME_FORMAT))  # 11時16分38秒
    print(get_japanese_weekday(jst_now.weekday()))  # 土
    print(get_japanese_weekday(jst_now.weekday(), True))  # 土曜日
