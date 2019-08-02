from redbot.core import data_manager
from .rio import Rio


def setup(bot):
    bot.add_cog(Rio())
