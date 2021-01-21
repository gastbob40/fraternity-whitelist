import discord


class OnVoiceStateUpdate:

    @staticmethod
    async def handle(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        pass
