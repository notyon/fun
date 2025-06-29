from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["start", "menu"]) & (filters.group | filters.private))
async def menu_handler(client: Client, message: Message):
    user = message.from_user.first_name
    await message.reply_text(
        f"👋 Hai {user}!\n\n"
        "Selamat datang di <b>FunBot</b>, bot hiburan seru untuk menemani aktivitasmu di grup ini. 🤖\n\n"
        "📋 <b>MENU BOT:</b>\n"
        "• <code>/jodoh</code> → Cari jodoh random di grup\n"
        "• <code>/cakep</code> → Tag random orang cakep di grup\n"
        "• <code>/jam</code> → Lihat jam di Indonesia, Korea & Rusia\n"
        "• <code>/rate</code> → Nilai acak untuk seseorang atau sesuatu\n"
        "• <code>/zodiak</code> → Tebakan zodiak random untukmu\n"
        "• <code>/menu</code> → Tampilkan menu ini kembali\n\n"
        "Silakan coba fiturnya dan have fun! 🎉",
        quote=True,
        parse_mode="html"
    )
