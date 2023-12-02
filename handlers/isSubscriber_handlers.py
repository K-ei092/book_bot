from aiogram import Router
from aiogram.types import Message
from filters.filters_subscriber import IsSubscriber

router = Router()


# Этот хэндлер будет реагировать на любые сообщения
# не от подписчиков канала "В Рифму",
# не предусмотренные логикой работы бота
@router.message(~IsSubscriber())
async def send_echo(message: Message):
    await message.answer(f'Привет!\n'
                         f'Подпишись на канал "В Рифму"\n'
                         f'https://t.me/+vZ_m6PB_c7wwNDky\n'
                         f'чтобы получить доступ к чтению')
