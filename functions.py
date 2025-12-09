from aiogram.types import Message
from aiogram import Bot

async def get_user_info(message : Message, bot : Bot):
    # Now i taking user dates
    user = await bot.get_chat(chat_id = message.from_user.id)

    matn = f"{message.from_user.mention_html('User')} info : \n\n"\
            f"User fullname : {message.from_user.full_name}\n"\
            f"User ID : <code>{message.from_user.id}</code>\n"

    if user.bio:
        matn += f"User bio : {user.bio}\n"
    if message.from_user.username:
        matn += f"Username : @{message.from_user.username}\n"
    
    # Now i get user photos
    photos = await message.from_user.get_profile_photos()
    
    if photos.photos:
        await message.answer_photo(photos.photos[0][-1].file_id, caption= matn, parse_mode = "HTML")
    else:
        await message.answer(matn, parse_mode = "HTML")
    