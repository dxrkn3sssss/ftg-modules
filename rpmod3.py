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
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit("<b>• чмок\n• чпок\n• кусь\n• обнять\n• шлеп\n• убить\n• выебать\n• связать\n• ударить\n• уебать\n• отсосать\n• отлизать\n• задушить\n• украсть\n• погладить\n• притянуть\n• изнасиловать\n• отпороть\n• кыш \n• дать \n• тьмок \n• споки \n• лав \n• мур \n• поцеловать \n• прижать \n• пнуть \n• рассенган\n• наказать\n• кря\n• дать котика\n• дать банан\n• сделать хохлом\n• подарить жёлтые тюльпаны\n• укусить\n• укусить за хуй\n• дать по жопе\n• скинуть нюдсы\n• дать конфету\n• уложить спать\n• разбудить\n• поворчать как бабка на\n• забрать в село на лето\n• купить мороженное</b>")

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
                    if message.text.lower() == "чпок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чпокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кусь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обнять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обнял(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
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
                    if message.text.lower() == "кыш":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прогнал(-а) прочь <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) по ебалу <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "тьмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> тьмокнул(-а) в щечку <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "споки":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пожелал(-а) спокойной ночи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "лав":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил(-а) любви <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "мур":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> муркнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "поцеловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцеловал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "прижать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прижал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "рассенган":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал(-а) рассенганом <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "наказать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> наказал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кря":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> хуякнул(-а) кря в личико <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать котик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) котика <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать банан":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) банан <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "сделать хохлом":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> сделал(-а) хохлом <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "подарить жёлтые тюльпаны":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил(-а) жёлтые тюльпаны <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "укусить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> укусил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "укусить за хуй":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> укусил(-а) за хуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать по жопе":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) по жопе <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "скинуть нюдсы":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> скинул(-а) нюдсы <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать конфету":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) конфету <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уложить спать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уложил(-а) спать <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "разбудить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> разбудил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "поворчать как бабка на":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поворчал(-а) как бабка на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "забрать в село на лето":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> забрал(-а) в село на лето <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "купить мороженное":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил(-а) мороженное <a href=tg://user?id={user.id}>{user.first_name}</a>")
        except: pass
