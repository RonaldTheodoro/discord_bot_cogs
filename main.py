import os

import discord
from discord.ext import commands


class Client(commands.Bot):
    extensions = ["cogs.cog01", "cogs.cog02", "cogs.cog03"]

    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("/"),
            intents=discord.Intents().all(),
        )

    async def setup_hook(self):
        print('Load cogs')
        for cog in self.extensions:
            print(f'Load {cog}')
            await self.load_extension(cog)

    async def on_ready(self):
        print("Bot start!")
        await self.tree.sync()
        print("UP")


client = Client()

client.run(os.getenv("BOT_TOKEN"))
