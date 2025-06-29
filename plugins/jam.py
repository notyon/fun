from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
import pytz

@Client.on_message(filters.command("jam") & (filters.group | filters.private))
async def jam_handler(client: Client, message: Message):
    zona_wib = pytz.timezone("Asia/Jakarta")
    zona_korea = pytz.timezone("Asia/Seoul")
    zona_rusia = pytz.timezone("Europe/Moscow")

    waktu_wib = datetime.now(zona_wib).strftime("%H:%M:%S")
    waktu_korea = datetime.now(zona_korea).strftime("%H:%M:%S")
    waktu_rusia = datetime.now(zona_rusia).strftime("%H:%M:%S")

    teks = (
        "🕒 Saat ini jam:\n\n"
        f"🇮🇩 Indonesia: {waktu_wib}\n"
        f"🇰🇷 Korea: {waktu_korea}\n"
        f"🇷🇺 Russia: {waktu_rusia}"
    )

    await message.reply_text(teks)
