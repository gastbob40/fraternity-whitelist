import discord

from src.utils.embeds_manager import EmbedsManager


class WhiteListQueue:
    requests = []
    client: discord.Client

    @staticmethod
    async def add_player(member: discord.Member):
        WhiteListQueue.requests.append(member.id)

        await member.send(
            embed=EmbedsManager.complete_embed(
                "Vous venez de rejoindre la file d'attente",
                f"Vous êtes en position **{len(WhiteListQueue.requests)}** dans la file d'attente.\n\n"
                f"Un staff s'occupera de vous dès qu'il sera disponible."
            )
        )
