import discord
import yaml

# Get configuration
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
                print(after.channel)

        # Case 2, the player leaves the channel
        if before.channel and before.channel.id == data['waiting_channel']:
            if after.channel is None or after.channel.id != data['waiting_channel']:
                print(before.channel)
