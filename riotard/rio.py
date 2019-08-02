from random import randrange
import discord

from redbot.core import commands
from redbot.core.data_manager import bundled_data_path


Cog = getattr(commands, "Cog", object)


class Riotard(Cog):
    """
    Says a random rio quote.
    """

    @commands.command()
    async def rio(self, ctx):
        """
        says a random rio quote
        """
        filepath = bundled_data_path(self) / "lines.txt"
        with filepath.open() as file:
            line = next(file)
            for num, readline in enumerate(file):
                if randrange(num + 2):
                    continue
                line = readline
        await ctx.maybe_send_embed(line)

