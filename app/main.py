# -*- code:utf-8 -*-
from localtime import japan


def main() -> None:
    jst_now = japan.get_curret_jst()
    date_str = jst_now.strftime(japan.DATE_FORMAT)
    time_str = jst_now.strftime(japan.TIME_FORMAT)
    print(f"今日は{date_str}。現在、{time_str}です。")


if __name__ == "__main__":
    main()
