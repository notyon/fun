import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command("jodoh") & filters.group)
async def jodoh_handler(client: Client, message: Message):
    chat_id = message.chat.id

    try:
        members = []
        async for m in client.get_chat_members(chat_id):
            if m.user.is_bot or m.user.is_deleted:
                continue
            members.append(m.user)

        if len(members) < 2:
            await message.reply_text("Tidak cukup anggota untuk dijodohkan 😅")
            return

        pasangan = random.sample(members, 2)
        user1 = pasangan[0]
        user2 = pasangan[1]

        mention1 = user1.mention if user1.username is None else f"@{user1.username}"
        mention2 = user2.mention if user2.username is None else f"@{user2.username}"

        await message.reply_text(
            f"💘 JODOH HARI INI 💘\n\n{mention1} ♥️ {mention2}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💘 Jodoh Saya", callback_data="jodoh_saya")]
            ])
        )

    except Exception as e:
        await message.reply_text("Gagal mencari jodoh. Cek apakah saya admin.")
        print(f"[ERROR /jodoh] {e}")

@Client.on_callback_query(filters.regex("jodoh_saya"))
async def jodoh_saya_callback(client: Client, callback_query: CallbackQuery):
    user = callback_query.from_user
    chat_id = callback_query.message.chat.id

    try:
        members = []
        async for m in client.get_chat_members(chat_id):
            if m.user.is_bot or m.user.is_deleted or m.user.id == user.id:
                continue
            members.append(m.user)

        if not members:
            await callback_query.answer("Tidak ada calon jodoh lain 😅", show_alert=True)
            return

        jodoh = random.choice(members)
        mention_user = user.mention if user.username is None else f"@{user.username}"
        mention_jodoh = jodoh.mention if jodoh.username is None else f"@{jodoh.username}"

        await callback_query.message.reply_text(
            f"💘 JODOH UNTUKMU 💘\n\n{mention_user} ❤️ {mention_jodoh}"
        )
        await callback_query.answer()

    except Exception as e:
        await callback_query.answer("Gagal mencari jodohmu 😢", show_alert=True)
        print(f"[ERROR tombol jodoh saya] {e}")
