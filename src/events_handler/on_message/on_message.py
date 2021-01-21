import discord


class OnMessage:
    @staticmethod
    async def handle(client: discord.Client, message: discord.Message):
        if message.author.bot:
            return
