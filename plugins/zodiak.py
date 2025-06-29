from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("zodiak") & (filters.group | filters.private))
async def zodiak_handler(client: Client, message: Message):
    zodiaks = [
        "♈ Aries", "♉ Taurus", "♊ Gemini", "♋ Cancer",
        "♌ Leo", "♍ Virgo", "♎ Libra", "♏ Scorpio",
        "♐ Sagittarius", "♑ Capricorn", "♒ Aquarius", "♓ Pisces"
    ]
    pilihan = random.choice(zodiaks)
    await message.reply_text(f"🔮 Aku menebak... Zodiak kamu adalah: *{pilihan}* ✨", parse_mode="markdown")
