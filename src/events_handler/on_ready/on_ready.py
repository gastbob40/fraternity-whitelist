import discord
from termcolor import colored


class OnReady:

    @staticmethod
    async def handle(client: discord.Client):
        print(
            colored("[FRaternity Support]", 'yellow'),
            colored(f"Logged in as {client.user} on {len(client.guilds)} servers", 'blue')
        )
