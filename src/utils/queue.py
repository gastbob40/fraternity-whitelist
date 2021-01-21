import discord
from termcolor import colored

from src.utils.embeds_manager import EmbedsManager


class WhiteListQueue:
    requests = []
    client: discord.Client

    @staticmethod
    def is_empty():
        return len(WhiteListQueue.requests) == 0

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

        print(
            colored("[FRaternity Whitelist]", 'yellow'),
            colored(
                f"{member.name}#{member.discriminator} ({member.id}) just join the queue at pos {len(WhiteListQueue.requests)}",
                'blue'
            )
        )

    @staticmethod
    async def remove_player(member: discord.Member):
        if member.id in WhiteListQueue.requests:
            WhiteListQueue.requests.remove(member.id)

        await member.send(
            embed=EmbedsManager.error_embed(
                "Vous venez de quitter la file d'attente",
                f"Vous perdez donc votre priorité dans la file d'attente."
            )
        )

        for i in range(len(WhiteListQueue.requests)):
            target: discord.User = await WhiteListQueue.client.fetch_user(WhiteListQueue.requests[i])

            await target.send(
                embed=EmbedsManager.complete_embed(
                    "Avancement dans la file d'attente",
                    f"Vous êtes maintenant en position **{i + 1}** dans la file d'attente.\n\n"
                )
            )
