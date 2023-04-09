
from telethon import *

from zthon import CMD_HELP
from zthon.utils import admin_cmd


# Fixed by zein
@borg.on(admin_cmd(pattern="بف ?(.*)"))
async def _(dc):

    d = dc.pattern_match.group(1)

    c = d.split(" ")

    chat_id = c[0]
    try:
        chat_id = int(chat_id)

    except BaseException:

        pass

    msg = ""
    masg = await dc.get_reply_message()  # zein😒😒
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit("⚜️الرساله وصلت يا كسول⚜️")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  # بشخر ضحك
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit("⚜️المسدج وصلت يكسول⚜️")
    except BaseException:  # بتعمل اي 🤔🤔
        await dc.edit(".بف (اليوزر) (الراساله)")


