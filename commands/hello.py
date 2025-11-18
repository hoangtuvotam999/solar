NAME = "hi"
ALIASES = ["hello", "2"]


async def handle(client, message, args):
    """
    example
    """
    thread_id = message.thread_id

    hello_msg_id = await client.send_message(
        text="hello 👋",
        thread_id=thread_id,
    )

    await client.react(
        reaction="❤️",
        message_id=message.id,
        thread_id=thread_id,
    )

    mem = getattr(client, "memory", {})
    mem["last_hello_msg_id"] = hello_msg_id
    client.memory = mem


async def on_message(client, message):
    """
    non-prefix
    """
    text = (message.text or "").strip().lower()
    if message.sender_id == client.uid:
        return

    if text == "hi":
        await client.send_message(
            text="hello 👋 (no prefix)",
            thread_id=message.thread_id,
        )
