import discord
from discord import app_commands
from discord.ext import commands


class Cog03(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="cog03", description="Sends hello")
    async def cog03(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="hello")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Cog03(client))
