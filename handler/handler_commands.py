import logging
from fbchat_muqit import EventType, Message
from commands import load_command_modules

logger = logging.getLogger("bot")

PREFIXES = ["/", "!", "."]


def register_handlers(client):
    modules = load_command_modules()

    # Map name/alias -> module
    name_map = {}
    for module in modules:
        name_map[module.NAME.lower()] = module
        for alias in getattr(module, "ALIASES", []):
            name_map[alias.lower()] = module

    @client.event(EventType.MESSAGE)
    async def on_message(message: Message):

        logger.info(f"|{message.sender_id}\n|text={message.text!r}")

        if message.sender_id == client.uid:
            return

        text = (message.text or "").strip()
        lower = text.lower()

        # PREFIX COMMAND
        for prefix in PREFIXES:
            if lower.startswith(prefix):
                rest = lower[len(prefix):].strip()
                if not rest:
                    return

                parts = rest.split()
                cmd = parts[0]
                args = parts[1:]

                module = name_map.get(cmd)
                if not module:
                    await client.send_message(
                        text=f"Không biết lệnh: {cmd}",
                        thread_id=message.thread_id,
                    )
                    return

                logger.info(f"DISPATCH | command={module.NAME} | args={args}")

                try:
                    await module.handle(client, message, args)
                except Exception as e:
                    logger.error(f"Lỗi command {module.NAME}: {e}")
                    await client.send_message(
                        text=f"❌ Lỗi khi xử lý lệnh `{module.NAME}`: {e}",
                        thread_id=message.thread_id,
                    )

                return

        # NON-PREFIX: command have on_message()
        for module in modules:
            if hasattr(module, "on_message"):
                try:
                    await module.on_message(client, message)
                except Exception as e:
                    logger.error(f"Lỗi on_message trong {module.NAME}: {e}")
