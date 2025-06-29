from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("rate") & (filters.group | filters.private))
async def rate_handler(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Apa yang mau dinilai? Contoh: /rate aku ganteng gak?")
        return

    target = message.text.split(None, 1)[1]
    nilai = random.randint(1, 100)

    await message.reply_text(f"Aku kasih nilai {nilai}% untuk: {target} 😄")
