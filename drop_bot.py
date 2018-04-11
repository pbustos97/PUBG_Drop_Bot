#!/usr/bin/python
import sys
import asyncio
import discord
import random
import time
from discord.ext import commands
import drop_bot_id
from drop_bot_id import pubg_drop_bot
import grid
from grid import grid
import location
from location import pubgmap

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='PlayerUnknown\'s Battlegrounds Drop Bot')

@bot.event
async def on_message(message):
    if message.content.startswith('pubg drop') and ' 1' in message.content:
        await bot.send_message(message.channel, pubgmap(1).format(message))
    elif message.content.startswith('pubg drop') and ' 2' in message.content:
        await bot.send_message(message.channel, pubgmap(2).format(message))
    elif message.content.startswith('pubg drop') and ' 3' in message.content:
        await bot.send_message(message.channel, pubgmap(3).format(message))
    elif message.content.startswith('pubg drop'):
        await bot.send_message(message.channel, 'Invalid Parameters!'.format(message))
    elif message.content.startswith('pubg grid'):
        if '1' or '2' in message.content:
            await bot.send_message(message.channel, grid(1).format(message))
        elif '3' in message.content:
            await bot.send_message(message.channel, grid(3).format(message))
        else:
            await bot.send_message(message.channel, 'Invalid Parameters!'.format(message))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(pubg_drop_bot)