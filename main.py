from rubpy.sync import Client, handlers, Message, models
from Advertise import Advertise


forward: bool = True
link: bool = True
RubinoPost: bool = True
StoryRubino: bool = True


def check_admins(group_guid, member_guid: str):
    admins = [i["member_guid"] for i in client.get_group_admin_members(group_guid)[
        'in_chat_members']]
    if member_guid in admins:
        return True


with Client(session='Account') as client:
    @client.on(handlers.MessageUpdates(models.is_group))
    def updates(message: Message):
        text = str(message)

        if Advertise.is_link(text):
            global link
            if link == True and not check_admins(message.object_guid, message.author_guid):
                client.ban_group_member(
                    message.object_guid, message.author_guid)
                client.delete_messages(message.object_guid, [
                                       message.message_id])
                message.reply(
                    "کاربر به دلیل ارسال لینک تبلیغاتی از گروه اخراج شد 🎊")

        elif Advertise.is_forwards(text):
            global forward
            if forward == True and not check_admins(message.object_guid, message.author_guid):
                client.ban_group_member(
                    message.object_guid, message.author_guid)
                client.delete_messages(message.object_guid, [
                                       message.message_id])
                message.reply(
                    "کاربر به دلیل ارسال پیام فرواردی از گروه اخراج شد 🎊")

        elif Advertise.is_RubinoPost(text):
            global RubinoPost
            if RubinoPost == True and not check_admins(message.object_guid, message.author_guid):
                client.ban_group_member(
                    message.object_guid, message.author_guid)
                client.delete_messages(message.object_guid, [
                                       message.message_id])
                message.reply(
                    "کاربر به دلیل ارسال پست روبینو از گروه اخراج شد 🎊")

        elif Advertise.is_StoryRubino(text):
            global StoryRubino
            if StoryRubino == True and not check_admins(message.object_guid, message.author_guid):
                client.ban_group_member(
                    message.object_guid, message.author_guid)
                client.delete_messages(message.object_guid, [
                                       message.message_id])
                message.reply(
                    "کاربر به دلیل ارسال استوری روبینو از گروه اخراج شد 🎊")

        elif message.raw_text == 'بازکردن فروارد':
            if check_admins(message.object_guid, message.author_guid):
                if forward != False:
                    forward = False
                    message.reply(
                        "اوکیه قفل فوروارد خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                else:
                    message.reply("قفل فروارد از قبل برداشته شده 🎊")

        elif message.raw_text == 'قفل فروارد':
            if check_admins(message.object_guid, message.author_guid):
                if forward != True:
                    forward = True
                    message.reply(
                        "اوکیه فوروارد قفل شد\nعمه هرکی فروارد بزنه🗿")
                else:
                    message.reply("قفل فروارد از قبل تنظیم شده 🎊")

        elif message.raw_text == 'قفل لینک':
            if check_admins(message.object_guid, message.author_guid):
                if link != True:
                    link = True
                    message.reply("اوکیه لینک قفل شد\nعمه هرکی لینک بفرسته🗿")
                else:
                    message.reply("قفل لینک از قبل تنظیم شده 🎊")

        elif message.raw_text == 'بازکردن لینک':
            if check_admins(message.object_guid, message.author_guid):
                if link != False:
                    link = False
                    message.reply(
                        "اوکیه قفل لینک خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                else:
                    message.reply("قفل لینک از قبل برداشته شده 🎊")

        elif message.raw_text == 'قفل پست روبینو':
            print(client.get_group_admin_access_list(
                message.object_guid, "u0GWoYm0749da990ea377480ae34b15c"))
            if check_admins(message.object_guid, message.author_guid):
                if RubinoPost != True:
                    RubinoPost = True
                    message.reply(
                        "اوکیه پست روبینو قفل شد\nعمه هرکی پست روبینو بفرسته🗿")
                else:
                    message.reply("قفل پست روبینو از قبل تنظیم شده 🎊")

        elif message.raw_text == 'بازکردن پست روبینو':
            if check_admins(message.object_guid, message.author_guid):
                if RubinoPost != False:
                    RubinoPost = False
                    message.reply(
                        "اوکیه قفل پست روبینو خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                else:
                    message.reply("قفل پست روبینو از قبل برداشته شده 🎊")

        elif message.raw_text == 'قفل استوری روبینو':
            if check_admins(message.object_guid, message.author_guid):
                if StoryRubino != True:
                    StoryRubino = True
                    message.reply(
                        "اوکیه استوری روبینو قفل شد\nعمه هرکی استوری روبینو بفرسته🗿")
                else:
                    message.reply("قفل استوری روبینو از قبل تنظیم شده 🎊")

        elif message.raw_text == 'بازکردن استوری روبینو':
            if check_admins(message.object_guid, message.author_guid):
                if StoryRubino != False:
                    StoryRubino = False
                    message.reply(
                        "اوکیه قفل استوری روبینو خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                else:
                    message.reply("قفل استوری روبینو از قبل برداشته شده 🎊")

        elif message.raw_text == 'وضعیت':
            group = client.get_group_info(message.object_guid)
            message.reply(f"✨ نام گروه : {group.group.group_title} \n\n🏀 تعداد اعضا  : {group.group.count_members}\n\nقفل لینک : {'              ✅' if link else '              ❌'}\n\nقفل فروارد : {'             ✅' if forward else '             ❌'}\n\nقفل پست روبینو : {'    ✅' if RubinoPost else '    ❌'}\n\nقفل استوری روبینو : {' ✅' if StoryRubino else ' ❌'}")

        elif message.raw_text == "راهنما":
            message.reply(
                "🧊 به راهنما داشوک خوش آمدید \n\nدستورات ربات : \n\n-** قفل لینک : **\n\n با فعال کردن این گزینه کاربر هایی که ادمین نیستند نباید لینک ارسال کنند چون ریمو میشن\n\n-** باز کردن لینک : **\n\nاگه دوست داشتید حساس بودن ربات به لینک رو غیر فعال کنید میتونید این متن رو بفرستید\n\n-** قفل فروارد **: \n\n با فعال کردن این گزینه میتونید پیام هایی که فروارد میشن توسط ربات حذف میشن \n\n-** بازکردن فروارد **: \n\nاگه دوست داشتید حالت حساسیت به پیام های فرواردی رو خاموش کنید میتونید این متن رو بفرستید \n\n-** قفل پست روبینو **: \n\nبا فعال کردن این گزینه کاربرا حق ندارن داخل گروه پست روبینو ارسال کنند \n\n-** بازکردن پست روبینو **:\n\nاگه خاستید واکنش ربات رو نسبت به پست های روبینو خاموش کنید این گزینه رو ارسال کنید \n\n- قفل استوری روبینو : \n\n با فعال کردن این گزینه اگه کاربری استوری روبینو بفرسته پیامش پاک میشه و کاربر اخراج میشه \n\n- بازکردن استوری روبینو :\n\nاگه خاستید واکنش ربات رو نسبت به استوری روبینو خاموش کنید این گزینه رو بفرستید \n\n〽️ برای دریافت اطلاعات گروه گزینه {وضعیت} رو میتونید ارسال کنید \n\n@smartcode01")

        elif message.raw_text == "بن":
            if check_admins(message.object_guid, message.author_guid):
                if message.reply_message_id != None:
                    message_data = client.get_messages_by_ID(
                        message.object_guid, [message.reply_message_id])
                    client.ban_group_member(
                        message.object_guid, message_data.messages[0].author_object_guid)
                    message.reply("کاربر از گروه اخراج شد 🎊")
                else:
                    message.reply("مدیر عزیز شما روی پیامی ریپلای نکردید")

        elif message.raw_text == "افزودن مدیر":
            """
            ['SetAdmin', 'BanMember', 'ChangeInfo', 'PinMessages', 'SetJoinLink', 'SetMemberAccess', 'DeleteGlobalAllMessages']
            """
            if check_admins(message.object_guid, message.author_guid):

                message_data = client.get_messages_by_ID(
                    message.object_guid, [message.reply_message_id])
                if not check_admins(message.object_guid, message_data.messages[0].author_object_guid):
                    client.set_group_admin(message.object_guid, message_data.messages[0].author_object_guid, access_list=[
                                           'DeleteGlobalAllMessages'])
                    message.reply("کاربر با موفقیت ادمین شد 🎊")
                else:
                    message.reply("کاربر از قبل ادمین میباشد 🎊")

        elif message.raw_text == "عذل مدیر":
            if check_admins(message.object_guid, message.author_guid):
                message_data = client.get_messages_by_ID(
                    message.object_guid, [message.reply_message_id])
                if check_admins(message.object_guid, message_data.messages[0].author_object_guid):
                    print(client.set_group_admin(message.object_guid, message_data.messages[0].author_object_guid, access_list=[
                          'DeleteGlobalAllMessages'], action="UnsetAdmin"))
                    message.reply("کاربر با موفقیت از لیست ادمین ها حذف شد 🎊")
                else:
                    message.reply("کاربر از قبل ادمین نمی باشد 🎊")


                    

    client.run_until_disconnected()
