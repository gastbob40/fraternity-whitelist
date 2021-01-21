import discord
import yaml

from src.events_handler.events_handler import EventsHandler

# Setup intents
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Get configuration
with open("run/config.yml", 'r') as stream:
    data = yaml.safe_load(stream)


@client.event
async def on_ready():
    await EventsHandler.handle_on_ready(client)


@client.event
async def on_message(message):
    await EventsHandler.handle_on_message(client, message)


# Start he bot
client.run(data['bot']['token'])
