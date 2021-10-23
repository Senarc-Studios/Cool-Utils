import discord
from discord.ext import commands

class Discord:
	class ColorConverter(commands.Converter):
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
					await ctx.send(f"{argument} is too, so it's going to 16777215 which is can use.")
					argument = 16777215

					#should change ctx.send to something else, so people will receive it in console instead

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