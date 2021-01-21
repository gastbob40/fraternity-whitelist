import discord
import yaml

# Get configuration
from src.events_handler.on_voice_state_update.channel_join import channel_join
from src.events_handler.on_voice_state_update.channel_leave import channel_leave

with open("run/config.yml", 'r') as stream:
    data = yaml.safe_load(stream)


class OnVoiceStateUpdate:

    @staticmethod
    async def handle(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if member.bot:
            return

        # Case 1, the player join the channel
        if after.channel and after.channel.id == data['waiting_channel']:
            if before.channel is None or before.channel.id != data['waiting_channel']:
                await channel_join(member)

        # Case 2, the player leaves the channel
        if before.channel and before.channel.id == data['waiting_channel']:
            if after.channel is None or after.channel.id != data['waiting_channel']:
                await channel_leave(member)
