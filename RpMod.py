from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""
    strings = {'name': 'RPMod'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <b>выключен</b></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <b>включен</b></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit("<b>• чмок\n•рп обнять\n• кляп\n• выебать как тварь\n• кусь\n• обнять\n• обнять2\n• обнять для иры\n• шлеп\n• убить\n• выебать\n• связать\n• ударить\n• уебать\n• отсосать\n• отлизать\n• задушить\n• украсть"
                           "\n• погладить\n• притянуть\n• изнасиловать\n• отпороть\n• наебать\n• поцеловать\n• накурить\n• набухать\n• засосать\n• утопить\n• расстрелять\n• прижать\n• понюхать\n• отдаться\n• покормить\n• кастрировать\n• пнуть\n• пожелать спокойной ночи\n• лизнуть\n• послать нахуй\n• ущипнуть\n• дать чапалаха\n• полюбить\n• признаться в любви\n• трахнуть\n• заебать\n• доебаться\n• дать бан\n• сделать шалавой</b>")

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "чмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "рп обнять":
                        await message.edit(f"<code> *нежно прижал головой к груди, целуя в макушку* </code> ")
                    if message.text.lower() == "кляп":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <code> связал, засунув кляп в рот, после чего отлупил плеткой </code> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выебать как тварь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выебал(-а) как тварь <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кусь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обнять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <code> обнял(-а) </code> <a href=tg://user?id={user.id}>{user.first_name}</code> </a>")
                    if message.text.lower() == "обнять для иры":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обнял(-а) <a href=tg://user?id={user.id}>{user.first_name}</code> </a>")
                    if message.text.lower() == "обнять2":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <code> крепко обнял(-а), осторожно поглаживая по плечу </code> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "шлеп":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> шлепнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "убить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> убил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "связать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ударить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ударил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отсосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал(-а) у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отлизать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отлизал(-а) у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "задушить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> задушил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "украсть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> украл(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "погладить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "притянуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> притянул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "изнасиловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> изнасиловал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отпороть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отпорол(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "наебать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> наебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>") 
                    if message.text.lower() == "поцеловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <code> поцеловал(-а) </code> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "накурить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> накурил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>") 
                    if message.text.lower() == "набухать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> набухал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "засосать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> засосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "утопить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> утопил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "расстрелять":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> расстрелял(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "прижать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прижал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "понюхать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> понюхал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отдаться":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отдался(-ась) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "покормить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> покормил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кастрировать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кастрировал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пожелать спокойной ночи":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пожелал(-а) спокойной ночи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "лизнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> лизнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послать нахуй":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал(-а) нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ущипнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ущипнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать чапалаха":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) чапалаха, с фразой: пиздуй рассылать клоун <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "полюбить":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> полюбил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "признаться в любви":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> признался(-ась) в любви <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "трахнуть":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> трахнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "заебать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> заебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "доебаться":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> доебался(-ась) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать бан":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) бан <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "сделать шалавой":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> сделал(-а) шалавой ебаной <a href=tg://user?id={user.id}>{user.first_name}</a>")
        except: pass
