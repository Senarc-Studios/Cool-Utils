import logging
import discord
from discord.ext import commands
from typing import TypeVar
import logging as log
import re
import aiohttp
import contextlib

log.getLogger(__name__)

MISSING = 0.0

__all__ = (
	'Discord'
)

T = TypeVar('T', bound='Discord')

class Discord:
	__all__ = (
		'ColourConverter',
		'ColorConverter',
		'EmojiBasic',
		'mutual_guild_check'
	)

	class ColourConverter(commands.Converter):
		async def convert(self, ctx, argument):

			try:
				color = await commands.ColourConverter().convert(ctx, argument)

			except commands.BadColourArgument:
				color = None

			if not color and not argument.isdigit():
				
				argument = list(s for s in argument.split(" ") if s)
					
			if color and argument.isdigit():
				argument = int(argument)

			if isinstance(argument, int):
				if argument > 16777215: 
					log.warning(f"{argument} is not valid color, 16777215 will be used instead.") # Shows a warning in console.
					argument = 16777215

				color = discord.Colour(argument)

			if isinstance(argument, list):

				argument = sorted(filter(lambda x: x.isdigit(), argument))

				argument = [int(n) for n in argument][:3]

				try:
					color = discord.Colour.from_rgb(*argument)
				
				except TypeError:
					color = None
			
			if color:
				if color.value > 16777215: 
					color = discord.Colour(16777215)
				
			return color

	def mutual_guild_check(author: discord.User, user: discord.User):
		mutual_guilds = set(author.mutual_guilds)
		mutual_guilds2 = set(user.mutual_guilds)

		return bool(mutual_guilds.intersection(mutual_guilds2))

	class EmojiBasic:
		def __init__(self, id: int, url: str):
			self.id = id
			self.url = url

		@classmethod
		async def convert(cls, ctx, argument):
			match = re.match(r'(?P<id>[0-9]{15,21})', argument)
			if match:
				emoji_id = (match.group(0))
				extensions = ["gif", "png"]
				code_list = [200, 201]
				
				async with aiohttp.ClientSession() as session:
					for extension in extensions:
						response = await session.get(f"https://cdn.discordapp.com/emojis/{emoji_id}.{extension}")
					
						if response.status in code_list:
							return cls(emoji_id, response.real_url)

						else:
							return None

	class BetterUserconverter(commands.Converter):
		async def convert(self, ctx, argument):
			try:
				user = await commands.UserConverter().convert(ctx, argument)

			except commands.UserNotFound:
				user = None

			if not user and ctx.guild:
				user = ctx.guild.get_member_named(argument)

			if user is None:
				role = None

				with contextlib.suppress(commands.RoleNotFound, commands.NoPrivateMessage):
					role = await commands.RoleConverter().convert(ctx, argument)
	  
				if role:
					if role.is_bot_managed():
						user = role.tags.bot_id
						user = ctx.bot.get_user(user) or await ctx.bot.fetch_user(user)

			if user is None:
				tag = re.match(r"#?(\d{4})",argument)
			
				if tag and not ctx.bot.users:
					test = discord.utils.get(ctx.bot.users, discriminator = tag.group(1))
					user = test or ctx.author
			
			return user

	class BetterMemberConverter(commands.Converter):
		async def convert(self, ctx, argument):
			try:
	  			user = await commands.MemberConverter().convert(ctx, argument)

			except commands.MemberNotFound:
	  			user = None

			if user is None:
		  		tag = re.match(r"#?(\d{4})", argument)
		  
			if tag:
				if ctx.guild:
					test = discord.utils.get(ctx.guild.members, discriminator = tag.group(1))
					user = test or ctx.author

			if ctx.guild is None:
				user = await self.BetterUserconverter().convert(ctx, argument)
				user = user or ctx.author

			return user	

Discord.ColorConverter = Discord.ColourCoverter