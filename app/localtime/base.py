# -*- code:utf-8 -*-
from pytz import BaseTzInfo
from datetime import datetime


def get_current_local_time(tz: BaseTzInfo) -> datetime:
    return datetime.now(tz)
