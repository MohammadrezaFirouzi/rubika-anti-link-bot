from rubpy import Client, handlers, Message, models
from asyncio import run

forward     :bool = True
link        :bool = True
RubinoPost  :bool = True
StoryRubino :bool = True
media       :bool = False    


class Advertise():

    async def is_forwards(text: str) -> bool:
        if 'forwarded_from' in text:
            return True

    async def is_RubinoPost(text: str) -> bool:
        if 'RubinoPost' in text:
            return True

    async def is_StoryRubino(text: str) -> bool:
        if 'RubinoStory' in text:
            return True

    async def is_link(text: str) -> bool:
        links: list = ['@', 'rubika']
        for link in links:
            if link in text:
                return True

    async def is_media(text : str) -> bool:
        if 'type": "FileInline' in text:
            return True

async def check_admins(client,group_guid, member_guid: str):
    data = await client.get_group_admin_members(group_guid)
    admins = [i["member_guid"] for i in data['in_chat_members']]
    if member_guid in admins:
        return True

async def main():
    async with Client(session='Account') as client:
        @client.on(handlers.MessageUpdates())
        async def updates(message: Message):
        
            text = str(message)

            if await Advertise.is_link(text):
                global link
                if link == True and not await check_admins(client ,message.object_guid, message.author_guid):
                    await client.ban_group_member(
                        message.object_guid, message.author_guid)
                    await client.delete_messages(message.object_guid, [
                                        message.message_id])
                    await message.reply(
                        "کاربر به دلیل ارسال لینک تبلیغاتی از گروه اخراج شد 🎊")

            elif await Advertise.is_forwards(text):
                global forward
                if forward == True and not await check_admins(client ,message.object_guid, message.author_guid):
                    await client.ban_group_member(
                        message.object_guid, message.author_guid)
                    await client.delete_messages(message.object_guid, [
                                        message.message_id])
                    await message.reply("کاربر به دلیل ارسال پیام فرواردی از گروه اخراج شد 🎊")

            elif await Advertise.is_RubinoPost(text):
                global RubinoPost
                if RubinoPost == True and not await check_admins(client ,message.object_guid, message.author_guid):
                    await client.ban_group_member(
                        message.object_guid, message.author_guid)
                    await client.delete_messages(message.object_guid, [
                                        message.message_id])
                    await message.reply(
                        "کاربر به دلیل ارسال پست روبینو از گروه اخراج شد 🎊")

            elif await Advertise.is_StoryRubino(text):
                global StoryRubino
                if StoryRubino == True and not await check_admins(client ,message.object_guid, message.author_guid):
                    await client.ban_group_member(message.object_guid, message.author_guid)
                    await client.delete_messages(message.object_guid, [message.message_id])
                    await message.reply("کاربر به دلیل ارسال استوری روبینو از گروه اخراج شد 🎊")

            elif await Advertise.is_media(text):
                global media
                if media == True and not await check_admins(client ,message.object_guid, message.author_guid):
                    await client.ban_group_member(message.object_guid, message.author_guid)
                    await client.delete_messages(message.object_guid, [message.message_id])
                    await message.reply("کاربر به دلیل ارسال مدیا از گروه اخراج شد 🎊")

            elif message.raw_text == 'بازکردن فروارد':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if forward != False:
                        forward = False
                        await message.reply(
                            "اوکیه قفل فوروارد خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                    else:
                        await message.reply("قفل فروارد از قبل برداشته شده 🎊")

            elif message.raw_text == 'قفل فروارد':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if forward != True:
                        forward = True
                        await message.reply(
                            "اوکیه فوروارد قفل شد\nعمه هرکی فروارد بزنه🗿")
                    else:
                        await message.reply("قفل فروارد از قبل تنظیم شده 🎊")

            elif message.raw_text == 'قفل لینک':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if link != True:
                        link = True
                        await message.reply("اوکیه لینک قفل شد\nعمه هرکی لینک بفرسته🗿")
                    else:
                        await message.reply("قفل لینک از قبل تنظیم شده 🎊")

            elif message.raw_text == 'بازکردن لینک':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if link != False:
                        link = False
                        await message.reply(
                            "اوکیه قفل لینک خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                    else:
                        await message.reply("قفل لینک از قبل برداشته شده 🎊")

            elif message.raw_text == 'قفل پست روبینو':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if RubinoPost != True:
                        RubinoPost = True
                        await message.reply(
                            "اوکیه پست روبینو قفل شد\nعمه هرکی پست روبینو بفرسته🗿")
                    else:
                        await message.reply("قفل پست روبینو از قبل تنظیم شده 🎊")

            elif message.raw_text == 'بازکردن پست روبینو':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if RubinoPost != False:
                        RubinoPost = False
                        await message.reply(
                            "اوکیه قفل پست روبینو خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                    else:
                        await message.reply("قفل پست روبینو از قبل برداشته شده 🎊")

            elif message.raw_text == 'قفل استوری روبینو':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if StoryRubino != True:
                        StoryRubino = True
                        await message.reply(
                            "اوکیه استوری روبینو قفل شد\nعمه هرکی استوری روبینو بفرسته🗿")
                    else:
                        await message.reply("قفل استوری روبینو از قبل تنظیم شده 🎊")

            elif message.raw_text == 'بازکردن استوری روبینو':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if StoryRubino != False:
                        StoryRubino = False
                        await message.reply(
                            "اوکیه قفل استوری روبینو خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                    else:
                        await message.reply("قفل استوری روبینو از قبل برداشته شده 🎊")


            elif message.raw_text == 'قفل مدیا':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if media != True:
                        media = True
                        await message.reply("اوکیه مدیا قفل شد\nعمه هرکی مدیا بفرسته🗿")
                    else:
                        await message.reply("قفل مدیا از قبل تنظیم شده 🎊")

            elif message.raw_text == 'بازکردن مدیا':
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if media != False:
                        media = False
                        await message.reply("اوکیه قفل مدیا خاموش شد\nدیگه عمه کسی در خطر نیست راحت باشین🗿")
                    else:
                        await message.reply("قفل مدیا از قبل برداشته شده 🎊")


            elif message.raw_text == 'وضعیت':
                group = await client.get_group_info(message.object_guid)
                await message.reply(f"✨ نام گروه : {group.group.group_title} \n\n🏀 تعداد اعضا  : {group.group.count_members}\n\nقفل لینک : {'              ✅' if link else '              ❌'}\n\nقفل فروارد : {'             ✅' if forward else '             ❌'}\n\nقفل پست روبینو : {'    ✅' if RubinoPost else '    ❌'}\n\nقفل استوری روبینو : {' ✅' if StoryRubino else ' ❌'}\n\nقفل مدیا : {'                ✅' if media else '                ❌'}")

            elif message.raw_text == "راهنما":
                await message.reply(
                    "🧊 به راهنما داشوک خوش آمدید \n\nدستورات ربات : \n\n-** قفل لینک : **\n\n با فعال کردن این گزینه کاربر هایی که ادمین نیستند نباید لینک ارسال کنند چون ریمو میشن\n\n-** باز کردن لینک : **\n\nاگه دوست داشتید حساس بودن ربات به لینک رو غیر فعال کنید میتونید این متن رو بفرستید\n\n-** قفل فروارد **: \n\n با فعال کردن این گزینه میتونید پیام هایی که فروارد میشن توسط ربات حذف میشن \n\n-** بازکردن فروارد **: \n\nاگه دوست داشتید حالت حساسیت به پیام های فرواردی رو خاموش کنید میتونید این متن رو بفرستید \n\n-** قفل پست روبینو **: \n\nبا فعال کردن این گزینه کاربرا حق ندارن داخل گروه پست روبینو ارسال کنند \n\n-** بازکردن پست روبینو **:\n\nاگه خاستید واکنش ربات رو نسبت به پست های روبینو خاموش کنید این گزینه رو ارسال کنید \n\n- قفل استوری روبینو : \n\n با فعال کردن این گزینه اگه کاربری استوری روبینو بفرسته پیامش پاک میشه و کاربر اخراج میشه \n\n- بازکردن استوری روبینو :\n\nاگه خاستید واکنش ربات رو نسبت به استوری روبینو خاموش کنید این گزینه رو بفرستید \n\n〽️ برای دریافت اطلاعات گروه گزینه {وضعیت} رو میتونید ارسال کنید \n\n@etrsbot")

            elif message.raw_text == "بن":
                if await check_admins(client ,message.object_guid, message.author_guid):
                    if message.reply_message_id != None:
                        message_data = await client.get_messages_by_ID(
                            message.object_guid, [message.reply_message_id])
                        await client.ban_group_member(
                            message.object_guid, message_data.messages[0].author_object_guid)
                        await message.reply("کاربر از گروه اخراج شد 🎊")
                    else:
                        await message.reply("مدیر عزیز شما روی پیامی ریپلای نکردید")



            elif message.raw_text == "افزودن مدیر":
                """
                ['SetAdmin', 'BanMember', 'ChangeInfo', 'PinMessages', 'SetJoinLink', 'SetMemberAccess', 'DeleteGlobalAllMessages']
                """
                if await check_admins(client ,message.object_guid, message.author_guid):

                    message_data = await client.get_messages_by_ID(
                        message.object_guid, [message.reply_message_id])
                    if not await check_admins(client,message.object_guid, message_data.messages[0].author_object_guid):
                        await client.set_group_admin(message.object_guid, message_data.messages[0].author_object_guid, access_list=[
                                            'DeleteGlobalAllMessages'])
                        await message.reply("کاربر با موفقیت ادمین شد 🎊")
                    else:
                        await message.reply("کاربر از قبل ادمین میباشد 🎊")




            elif message.raw_text == "عذل مدیر":
                if await check_admins(client ,message.object_guid, message.author_guid):
                    message_data = await client.get_messages_by_ID(
                        message.object_guid, [message.reply_message_id])
                    if check_admins(message.object_guid, message_data.messages[0].author_object_guid):
                        await client.set_group_admin(message.object_guid, message_data.messages[0].author_object_guid, access_list=[
                            'DeleteGlobalAllMessages'], action="UnsetAdmin")
                        await message.reply("کاربر با موفقیت از لیست ادمین ها حذف شد 🎊")
                    else:
                        await message.reply("کاربر از قبل ادمین نمی باشد 🎊")


                        

        await client.run_until_disconnected()

run(main())
