from .. import loader, utils

class CityWars2DrawingMod(loader.Module):
    """Модуль ловли подарков в CityWars2.0 Chat."""
    strings = {'name': 'CityWars2Drawing'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("CityWars2Drawing", "status", True)

    async def cdtcmd(self, message):
        """Используй: .cd2 чтобы включить/выключить ловлю подарков."""
        status = self.db.get("CityWars2Drawing", "status")
        if status is not True:
            await message.edit("<b>Ловля подарков CityWars2.0 Chat:</b> <code>Включена</code>")
            self.db.set("CityWars2Drawing", "status", True)
        else:
            await message.edit("<b>Ловля подарков CityWars2.0 Chat:</b> <code>Отключена</code>")
            self.db.set("CityWars2Drawing", "status", False)

    async def watcher(self, message):
        try:
            status = self.db.get("CityWars2Drawing", "status")
            me = (await message.client.get_me()).id
            if status:
                if message.chat_id == CityWars2:
                    click = (await message.click(0)).message
                    await message.client.send_message(me, f"Словлен подарок в CityWars2.0 Chat:\n\n{click}")
        except: pass