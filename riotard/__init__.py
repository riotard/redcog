from redbot.core import data_manager
from .riotard import Riotard


def setup(bot):
    bot.add_cog(Skyrim())
