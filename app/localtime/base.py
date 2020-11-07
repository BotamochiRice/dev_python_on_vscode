# -*- code:utf-8 -*-
from pytz import BaseTzInfo
from datetime import datetime


def get_current_local_time(tz: BaseTzInfo) -> datetime:
    """This returns current local time based on the given timezone.

    Args:
        tz (BaseTzInfo): timezone where you want the current local time

    Returns:
        datetime: current local time based on the given timezone.
    """
    return datetime.now(tz)
