import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio
import os
from dotenv import load_dotenv

load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print("Token tidak ditemukan dalam file .env")
    exit()  

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

song_queue = []

@bot.event
async def on_ready():
    print(f'Bot telah login sebagai {bot.user}')

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("Anda harus berada di voice channel!")
        return
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f"Bot bergabung dengan {channel.name}")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Bot telah keluar dari voice channel.")
    else:
        await ctx.send("Bot tidak berada di voice channel!")

@bot.command()
async def play(ctx, *, search: str):
    vc = ctx.voice_client
    if not vc:
        await ctx.invoke(join)
        vc = ctx.voice_client

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search}", download=False)['entries'][0]
        url = info['url']
        title = info['title']

    song_queue.append((title, url))
    if not vc.is_playing():
        await play_next(ctx)

async def play_next(ctx):
    vc = ctx.voice_client
    if song_queue:
        title, url = song_queue.pop(0)
        ffmpeg_opts = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        vc.play(
            discord.FFmpegPCMAudio(url, **ffmpeg_opts),
            after=lambda e: bot.loop.call_soon_threadsafe(asyncio.create_task, play_next(ctx))
        )
        await ctx.send(f"Memutar: **{title}**")
    else:
        await ctx.send("Daftar lagu kosong. Bot keluar dari voice channel.")
        await vc.disconnect()

@bot.command()
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Musik dilewati!")
        await play_next(ctx)

@bot.command()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        song_queue.clear()
        await ctx.send("Musik dihentikan dan daftar lagu dibersihkan.")
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("Tidak ada musik yang sedang diputar.")

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f'Error: {e}')
