import discord
import yaml

from src.utils.embeds_manager import EmbedsManager
from src.utils.queue import WhiteListQueue

# Get configuration
with open("run/config.yml", 'r') as stream:
    data = yaml.safe_load(stream)


class OnMessage:
    @staticmethod
    async def handle(client: discord.Client, message: discord.Message):
        if message.author.bot or isinstance(message.author, discord.User):
            return

        if message.content == '!next':
            await take_whitelist(client, message)


async def take_whitelist(client: discord.Client, message: discord.Message):
    if message.channel.id != data['command_channel']:
        return

    if not message.author.permissions_in(message.channel).manage_messages:
        return await message.author.send(
            embed=EmbedsManager.error_embed(
                "Erreur",
                "Vous n'avez pas les permissions nécessaires"
            )
        )

    if message.author.voice is None:
        return await message.author.send(
            embed=EmbedsManager.error_embed(
                "Erreur",
                "Vous devez être connecté en vocal pour faire une whitelist."
            )
        )

    if WhiteListQueue.is_empty():
        return await message.author.send(
            embed=EmbedsManager.error_embed(
                "Erreur",
                "Il n'y a personne à faire passer."
            )
        )

    await WhiteListQueue.take_player(message.author)
