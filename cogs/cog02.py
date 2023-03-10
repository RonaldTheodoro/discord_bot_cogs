import discord
from discord import app_commands
from discord.ext import commands


class Cog02(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="cog02", description="Sends hello")
    async def cog02(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="hello")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Cog02(client))
