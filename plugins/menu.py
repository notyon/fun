from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["start", "menu"]) & (filters.group | filters.private))
async def menu_handler(client: Client, message: Message):
    await message.reply_text(
        "📋 MENU BOT:\n"
        "- /jodoh → Cari jodoh random di grup\n"
        "- /menu → Tampilkan menu"
    )
