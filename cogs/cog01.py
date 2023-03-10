import discord
from discord import app_commands
from discord.ext import commands


class Cog01(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="cog01", description="Sends hello")
    async def cog01(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="hello")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Cog01(client))
