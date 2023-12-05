# TG-invite-bot
Бота для Telegram, который перемещает пользователей из одной группы в другую. Важно отметить, что автоматически добавлять пользователей в группы без их явного согласия может нарушать правила Telegram и привести к ограничениям для вашего бота. Убедитесь, что у вас есть разрешение от всех участников.

Вот шаги, которые вам нужно сделать:

1. Создать бота в Telegram:
   - Используйте BotFather в Telegram для создания нового бота и получения токена API.

2. Настроить среду разработки:
   - Установите Python и библиотеку python-telegram-bot.
   - Установите telethon или любую другую библиотеку, которая поддерживает работу с Telegram API на уровне пользователя.

3. Создать скрипт для бота:
   - Используйте Telegram API для доступа к списку участников группы и их добавления в другую группу.
   - Учтите ограничения Telegram по количеству добавлений в группу в определенный промежуток времени.

4. Развертывание и запуск бота:
   - Разверните бота на сервере или локальной машине.
   - Запустите бота и убедитесь, что он работает правильно.

Теперь давайте рассмотрим код на Python с использованием библиотеки telethon:

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'
client = TelegramClient('session_name', api_id, api_hash)

client.start(phone=phone)

async def add_users(source_group, target_group):
    # Получение списка участников из исходной группы
    source_group_entity = await client.get_entity(source_group)
    source_members = await client.get_participants(source_group_entity)

    # Получение объекта целевой группы
    target_group_entity = await client.get_entity(target_group)

    # Добавление участников в целевую группу
    for user in source_members:
        try:
            print(f"Добавление {user.id} в {target_group}")
            await client(InviteToChannelRequest(target_group_entity, [user]))
        except Exception as e:
            print(e)
            continue

# Замените 'source_group' и 'target_group' на названия или ID ваших групп
with client:
    client.loop.run_until_complete(add_users('source_group', 'target_group'))


Важные замечания:
- Замените 'YOUR_API_ID', 'YOUR_API_HASH', 'YOUR_PHONE_NUMBER', 'session_name', 'source_group' и 'target_group' на реальные значения.
- Этот код предполагает, что у вас уже есть api_id и api_hash, которые можно получить через приложение Telegram.
- Код должен быть запущен в асинхронном режиме, так как операции с сетью могут занять некоторое время.
- Обработка ошибок в этом коде минимальна, вам нужно будет добавить соответствующую логику обработки ошибок, чтобы управлять такими ситуациями, как ограничение на добавление пользователей.
- Помните о правилах и ограничениях Telegram, чтобы избежать блокировки вашего бота.
