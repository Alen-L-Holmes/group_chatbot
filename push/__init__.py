from pathlib import Path

import nonebot
from nonebot import get_driver

from .config import Config

from nonebot import require
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import MessageSegment

from .call_interface import get_slack_off_calendar

global_config = get_driver().config
config = Config.parse_obj(global_config)

group_id = config.group_id
hour = config.hour
minute = config.minute

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass

scheduler_slack_off_calendar = require('nonebot_plugin_apscheduler').scheduler


async def slack_off_calendar_handle():
    for i in group_id:
        bot = nonebot.get_bot()
        await bot.send_msg(message_type='group', sub_type='normal', group_id=i, message='今日份摸鱼日历已送达')
        await bot.send_msg(message_type='group', sub_type='normal', group_id=i, message=MessageSegment.image(file=get_slack_off_calendar()))


scheduler_slack_off_calendar.add_job(slack_off_calendar_handle, 'cron', timezone='Asia/Shanghai', hour=hour, minute=minute)


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(str((Path(__file__).parent / "plugins").resolve()))
