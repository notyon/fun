from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("hajar") & (filters.group | filters.private))
async def hajar_handler(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply_text("Harus reply pesan seseorang untuk dihajar!")
        return

    target_user = message.reply_to_message.from_user
    if target_user.is_bot:
        await message.reply_text("ngapain hajar gua? 😅")
        return

    variasi = ["TAMPAR", "HANTAM", "TABOK", "BANTAI", "TENDANG", "HAJAR", "PUKUL"]
    kata = random.choice(variasi)
    mention = target_user.mention()

    await message.reply_text(f"GUA {kata} LU {mention} !")
