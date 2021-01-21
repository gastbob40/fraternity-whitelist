import discord

from src.utils.queue import WhiteListQueue


async def channel_leave(member: discord.Member):
    await WhiteListQueue.remove_player(member)
