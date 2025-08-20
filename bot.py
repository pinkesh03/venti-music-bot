from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import os

# Environment variables from Sevalla
API_ID = int(os.environ.get("25266590"))
API_HASH = os.environ.get("1c662b76c01d299137cdc8acd321fa24")
BOT_TOKEN = os.environ.get("8301651341:AAFk3bD_TJ4QsyZhuUT-wLEcYMCaJCJ5iao")
SESSION_STRING = os.environ.get("BQGBiZ4AITTPV6qbswig20N28DKpnD35kcZB8HLZprPtymNxjtCvLgmevcbC5MZ3M3GsoCOWhlKeygIzTHwc3mmPP_NyF8H_n369MdJxphBYPwp8Am9L4ohwrFKVa6F9ZU_QUv94UwL4tz5XFUHvM1uc6igm9Lo6AM-Dx0277vo1QAflJaOOjEyGTNS1w9FI_xsVSibuc2HNRBlfcKU8JD2GNGh2JSEgN24KL2taBp_3A6ugWbFSYxNM8ReK5dzafv4TwAxODfUV2c_SopIcsHBNBspqG2-m9XTmvl5AX6_8mU81gnP1LKWbZD5wB4c1ft2M0DRqcsuMWBIAVF53_k_Dl62iFQAAAAHZRKJHAA")

# Bot client
app = Client(
    "venti_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Voice Chat client
call = PyTgCalls(app)

# Start command
@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("🎶 Venti Music Bot is online! Use /play <url> to stream music.")

# Play command
@app.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply_text("⚠ Please give me an audio/video URL to play.")
    
    link = message.command[1]
    await call.join_group_call(
        message.chat.id,
        AudioPiped(link)
    )
    await message.reply_text(f"▶ Playing: {link}")

# Run bot
app.start()
call.start()
print("✅ Bot Started")
app.idle()
