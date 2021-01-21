import discord

from src.events_handler.on_message.on_message import OnMessage
from src.events_handler.on_ready.on_ready import OnReady
from src.events_handler.on_voice_state_update.on_voice_state_update import OnVoiceStateUpdate


class EventsHandler:

    @staticmethod
    async def handle_on_ready(client: discord.Client):
        await OnReady.handle(client)

    @staticmethod
    async def handle_on_message(client, message):
        await OnMessage.handle(client, message)

    @staticmethod
    async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        await OnVoiceStateUpdate.handle(member, before, after)
