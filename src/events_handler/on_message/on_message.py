import discord

from src.utils.embeds_manager import EmbedsManager
from src.utils.queue import WhiteListQueue


class OnMessage:
    @staticmethod
    async def handle(client: discord.Client, message: discord.Message):
        if message.author.bot:
            return

        if message.content == '!next':
            await take_whitelist(client, message)


async def take_whitelist(client: discord.Client, message: discord.Message):
    if message.author.voice is None:
        await message.author.send(
            embed=EmbedsManager.error_embed(
                "Erreur",
                "Vous devez être connecté en vocal pour faire une whitelist."
            )
        )

    if WhiteListQueue.is_empty():
        await message.author.send(
            embed=EmbedsManager.error_embed(
                "Erreur",
                "Il n'y a personne à faire passer."
            )
        )
