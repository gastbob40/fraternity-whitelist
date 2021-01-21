import discord

from src.events_handler.on_message.on_message import OnMessage
from src.events_handler.on_ready.on_ready import OnReady


class EventsHandler:

    @staticmethod
    async def handle_on_ready(client: discord.Client):
        await OnReady.handle(client)

    @staticmethod
    async def handle_on_message(client, message):
        await OnMessage.handle(client, message)
