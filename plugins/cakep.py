from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("cakep") & filters.group)
async def cakep_handler(client: Client, message: Message):
    try:
        members = [m async for m in client.get_chat_members(message.chat.id, limit=200)]
        users = [m.user for m in members if not m.user.is_bot]

        if not users:
            await message.reply_text("Tidak ada anggota yang bisa dipilih 😢")
            return

        chosen = random.choice(users)
        mention = chosen.mention(style="md")
        await message.reply_text(
            f"🌟 ORANG CAKEP HARI INI: {mention}",
            parse_mode="markdown"
        )

    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {e}")
