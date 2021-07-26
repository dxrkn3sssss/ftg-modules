from .. import loader, utils

class CityWars1DrawingMod(loader.Module):
    """Модуль ловли подарков в City Wars News."""
    strings = {'name': 'CityWars1Drawing'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("CityWars1Drawing", "status", True)

    async def cdcmd(self, message):
        """Используй: .cd чтобы включить/выключить ловлю подарков."""
        status = self.db.get("CityWars1Drawing", "status")
        if status is not True:
            await message.edit("<b>Ловля подарков City Wars News:</b> <code>Включена</code>")
            self.db.set("CityWars1Drawing", "status", True)
        else:
            await message.edit("<b>Ловля подарков City Wars News:</b> <code>Отключена</code>")
            self.db.set("CityWars1Drawing", "status", False)

    async def watcher(self, message):
        try:
            status = self.db.get("CityWars1Drawing", "status")
            me = (await message.client.get_me()).id
            if status:
                if message.chat_id == -1001101812774:
                    click = (await message.click(0)).message
                    await message.client.send_message(me, f"Словлен подарок в City Wars News")
        except: pass