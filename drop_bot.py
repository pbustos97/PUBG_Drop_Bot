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

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='PlayerUnknown\'s Battlegrounds Drop Bot')

# number of locations per map
map1 = (26 - 1)
map2 = (32 - 1)

@bot.event
async def on_message(message):
    if message.content.startswith('pubg drop') and '1' in message.content:
        rando = random.randint(0,map1)
        if (rando == 0):
            await bot.send_message(message.channel, 'Zharki'.format(message))
        elif (rando == 1):
            await bot.send_message(message.channel, 'Georgopol'.format(message))
        elif (rando == 2):
            await bot.send_message(message.channel, 'Hospital'.format(message))
        elif (rando == 3):
            await bot.send_message(message.channel, 'Gatka'.format(message))
        elif (rando == 5):
            await bot.send_message(message.channel, 'Quarry'.format(message))
        elif (rando == 6):
            await bot.send_message(message.channel, 'Primorsk'.format(message))
        elif (rando == 7):
            await bot.send_message(message.channel, 'Ferry Pier'.format(message))
        elif (rando == 8):
            await bot.send_message(message.channel, 'Pochinki'.format(message))
        elif (rando == 9):
            await bot.send_message(message.channel, 'Ruins'.format(message))
        elif (rando == 10):
            await bot.send_message(message.channel, 'Rozhok'.format(message))
        elif (rando == 11):
            await bot.send_message(message.channel, 'School'.format(message))
        elif (rando == 12):
            await bot.send_message(message.channel, 'School Apartments'.format(message))
        elif (rando == 13):
            await bot.send_message(message.channel, 'Shooting Range'.format(message))
        elif (rando == 14):
            await bot.send_message(message.channel, 'Severny'.format(message))
        elif (rando == 15):
            await bot.send_message(message.channel, 'Stalbar'.format(message))
        elif (rando == 16):
            await bot.send_message(message.channel, 'Yasnaya Polyana'.format(message))
        elif (rando == 17):
            await bot.send_message(message.channel, 'Mansion'.format(message))
        elif (rando == 18):
            await bot.send_message(message.channel, 'Shelter'.format(message))
        elif (rando == 19):
            await bot.send_message(message.channel, 'Prison'.format(message))
        elif (rando == 20):
            await bot.send_message(message.channel, 'Mylta'.format(message))
        elif (rando == 21):
            await bot.send_message(message.channel, 'Farm'.format(message))
        elif (rando == 22):
            await bot.send_message(message.channel, 'Mylta Power'.format(message))
        elif (rando == 23):
            await bot.send_message(message.channel, 'Lipovka'.format(message))
        elif (rando == 24):
            await bot.send_message(message.channel, 'Kameshki'.format(message))
        elif (rando == 25):
            await bot.send_message(message.channel, 'Novorepnoye'.format(message))
        elif (rando == 26):
            await bot.send_message(message.channel, 'Sosnovka Military Base'.format(message))
    elif message.content.startswith('pubg drop') and '2' in message.content:
        rando = random.randint(0,map2)
        if (rando == 0):
            await bot.send_message(message.channel, 'Campo Militar'.format(message))
        elif (rando == 1):
            await bot.send_message(message.channel, 'Tierra Bronca'.format(message))
        elif (rando == 2):
            await bot.send_message(message.channel, 'El Azahar'.format(message))
        elif (rando == 3):
            await bot.send_message(message.channel, 'Impala'.format(message))
        elif (rando == 4):
            await bot.send_message(message.channel, 'Puerto Paraiso'.format(message))
        elif (rando == 5):
            await bot.send_message(message.channel, 'North Island'.format(message))
        elif (rando == 6):
            await bot.send_message(message.channel, 'South Island'.format(message))
        elif (rando == 7):
            await bot.send_message(message.channel, 'Tiny Isand'.format(message))
        elif (rando == 8):
            await bot.send_message(message.channel, 'Los Leones'.format(message))
        elif (rando == 9):
            await bot.send_message(message.channel, 'La Bendita'.format(message))
        elif (rando == 10):
            await bot.send_message(message.channel, 'Junkyard'.format(message))
        elif (rando == 11):
            await bot.send_message(message.channel, 'Minas Generales'.format(message))
        elif (rando == 12):
            await bot.send_message(message.channel, 'Graveyard'.format(message))
        elif (rando == 13):
            await bot.send_message(message.channel, 'Hacienda del Patron'.format(message))
        elif (rando == 14):
            await bot.send_message(message.channel, 'Cruz del Valle'.format(message))
        elif (rando == 15):
            await bot.send_message(message.channel, 'Torre Ahumada'.format(message))
        elif (rando == 16):
            await bot.send_message(message.channel, 'Water Treatment'.format(message))
        elif (rando == 17):
            await bot.send_message(message.channel, 'San Martin'.format(message))
        elif (rando == 18):
            await bot.send_message(message.channel, 'Power Grid'.format(message))
        elif (rando == 19):
            await bot.send_message(message.channel, 'Pecado'.format(message))
        elif (rando == 20):
            await bot.send_message(message.channel, 'Chumacera'.format(message))
        elif (rando == 21):
            await bot.send_message(message.channel, 'Minas del Valle'.format(message))
        elif (rando == 22):
            await bot.send_message(message.channel, 'Los Higos'.format(message))
        elif (rando == 23):
            await bot.send_message(message.channel, 'Prison'.format(message))
        elif (rando == 24):
            await bot.send_message(message.channel, 'Minas del Sur'.format(message))
        elif (rando == 25):
            await bot.send_message(message.channel, 'Valle del Mar'.format(message))
        elif (rando == 26):
            await bot.send_message(message.channel, 'Monte Nuevo'.format(message))
        elif (rando == 27):
            await bot.send_message(message.channel, 'Ladrillera'.format(message))
        elif (rando == 28):
            await bot.send_message(message.channel, 'El Pozo'.format(message))
        elif (rando == 29):
            await bot.send_message(message.channel, 'Trailer Park'.format(message))
        elif (rando == 30):
            await bot.send_message(message.channel, 'Ruins'.format(message))
        elif (rando == 31):
            await bot.send_message(message.channel, 'La Cobreria'.format(message))
        elif (rando == 32):
            await bot.send_message(message.channel, 'Crater Fields'.format(message))
    elif message.content.startswith('pubg drop'):
        await bot.send_message(message.channel, 'Invalid Parameters!'.format(message))
    elif message.content.startswith('pubg grid'):
        if '1' in message.content:
            await bot.send_message(message.channel, grid(1).format(message))
        elif '2' in message.content:
            await bot.send_message(message.channel, grid(2).format(message))
        else:
            await bot.send_message(message.channel, 'Invalid Parameters!'.format(message))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(pubg_drop_bot)