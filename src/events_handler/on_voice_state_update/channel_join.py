import discord

from src.utils.queue import WhiteListQueue


async def channel_join(member: discord.Member):
    await WhiteListQueue.add_player(member)
