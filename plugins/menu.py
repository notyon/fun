from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["start", "menu"]) & (filters.group | filters.private))
async def menu_handler(client: Client, message: Message):
    user = message.from_user.first_name
    await message.reply_text(
        f"👋 Hai {user}!\n\n"
        "Selamat datang di *FunBot*, bot hiburan seru untuk menemani aktivitasmu di grup ini. 🤖\n\n"
        "📋 *MENU BOT:*\n"
        "• `/jodoh` → Cari jodoh random di grup\n"
        "• `/cakep` → Tag random orang cakep di grup\n"
        "• `/jam` → Lihat jam di Indonesia, Korea & Rusia\n"
        "• `/rate` → Nilai acak untuk seseorang atau sesuatu\n"
        "• `/zodiak` → Tebakan zodiak random untukmu\n"
        "• `/menu` → Tampilkan menu ini kembali\n\n"
        "Silakan coba fiturnya dan have fun! 🎉",
        quote=True,
        parse_mode="markdown"
    )
