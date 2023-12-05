from telethon import TelegramClient, events, sync

# Эти данные необходимо получить на my.telegram.org
api_id = 'ВАШ_API_ID'
api_hash = 'ВАШ_API_HASH'

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)

# Асинхронная функция для копирования участников
async def copy_members(from_chat, to_chat):
    # Получаем информацию о чатах
    from_chat = await client.get_input_entity(from_chat)
    to_chat = await client.get_input_entity(to_chat)
    
    # Получаем всех участников чата
    members = await client.get_participants(from_chat)
    
    # Добавляем участников в новый чат
    for member in members:
        try:
            await client.edit_admin(to_chat, member, is_admin=True)
            print(f"Участник {member.id} добавлен.")
        except Exception as e:
            print(f"Не удалось добавить {member.id}: {e}")
        await asyncio.sleep(1)  # Задержка для избежания ограничений

# Запуск клиента
with client:
    client.loop.run_until_complete(copy_members('ИСХОДНЫЙ_ЧАТ', 'ЦЕЛЕВОЙ_ЧАТ'))
