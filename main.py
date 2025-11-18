import os
import logging
from fbchat_muqit import Client
from handler.handler_commands import register_handlers

COOKIES_FILE_PATH = "cookies.json"

def clear_logging():
    _logger = ["fbchat-muqit","solar"]
    for name in _logger:
        logging.getLogger(name).setLevel(logging.CRITICAL)
        logging.getLogger(name).propagate = False

    logging.basicConfig(
        level=logging.INFO,
        format="[BOT] %(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
    )

def create_client():
    if not os.path.exists(COOKIES_FILE_PATH):
        raise FileNotFoundError(f"cookies err: {COOKIES_FILE_PATH} ?")
    return Client(cookies_file_path=COOKIES_FILE_PATH)


def main():
    clear_logging()
    logger = logging.getLogger("bot")

    client = create_client()
    logger.info("hello world !!!\nI'm solar bots.")
    register_handlers(client)
    logger.info("Starting bot…")
    client.run()

if __name__ == "__main__":
    main()