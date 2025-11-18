# solar
Bot messenger uses Facebook's unofficial API

Dưới đây là bản **README.md song ngữ (EN + VI)** theo yêu cầu của bạn:

* Mở đầu: *“File README này được viết bằng ChatGPT”*
* Có tiếng Anh và tiếng Việt
* Giữ phong cách “muốn gì tự làm thêm, không có update đâu”

Bạn có thể copy-paste nguyên file.

---

# 📌 README

*(File README này được viết bằng ChatGPT)*

---

# 🇬🇧 English Version

## Simple Modular Command System for fbchat-muqit Bot

This project implements a **very simple, modular command system** built on top of **fbchat-muqit**.
It does not include advanced features, auto-updates, plugins, or any kind of framework magic.

👉 **If you want more features, write your own commands.
There will be no updates here.**

Project is based on the excellent library:
[https://github.com/togashigreat/fbchat-muqit](https://github.com/togashigreat/fbchat-muqit)

---

## 🚀 How It Works

* `main.py`
  Initializes the bot, sets clean logging, registers handlers.

* `handler/handler_commands.py`
  A single unified router:

  * Logs all incoming messages
  * Parses prefix commands (`/`, `!`, `.`)
  * Dispatches the correct command module
  * For non-prefix messages, it calls `on_message()` in each module (if provided)

* `commands/`
  Every `.py` file is a self-contained command module.

There is no abstraction and no hidden behavior — what you write is exactly what runs.

---

## 🧩 How to Write Your Own Commands

Just create a file inside the `commands/` folder.

Example structure:

```python
NAME = "yourcmd"
ALIASES = ["alias1", "alias2"]

async def handle(client, message, args):
    await client.send_message(
        text=f"Command executed with args: {args}",
        thread_id=message.thread_id,
    )
```

### Optional: Handle normal (non-prefix) chat

```python
async def on_message(client, message):
    text = (message.text or "").lower()
    if text == "hello":
        await client.send_message(
            text="Hi there!",
            thread_id=message.thread_id,
        )
```

Restart the bot → the new command is active.

---

## 🧪 Minimal Example

`commands/ping.py`:

```python
NAME = "ping"
ALIASES = ["p"]

async def handle(client, message, args):
    await client.send_message(
        text="pong!",
        thread_id=message.thread_id,
    )
```

Use:

```
/ping
/p
```

---

## ⚙️ Prefix Syntax

The bot supports:

```
/command
!command
.command
```

Arguments are automatically parsed:

```
/echo hello world
→ args = ["hello", "world"]
```

---

## 🛑 No Auto-Updates

This is not a framework.
This is not a plugin engine.
It is intentionally simple.

> **You want something new → you write a command.
> You want automation → you write a command.
> You want AI → you write a command.**

The project will not update itself.
You are the one who extends it.

---

## 📁 Project Structure

```
.
├── main.py
├── handler/
│   └── handler_commands.py
└── commands/
    ├── ping.py
    ├── hi.py
    ├── anh.py
    └── your_command_here.py
```

---

# 🇻🇳 Phiên Bản Tiếng Việt

## Hệ thống command đơn giản cho bot fbchat-muqit

Dự án này là một hệ thống command **rất đơn giản, dễ mở rộng**, chạy trên nền **fbchat-muqit**.
Không phải framework, không có plugin engine, không có update tự động.

👉 **Muốn thêm chức năng gì thì tự viết command mới.
Ở đây sẽ không có bản cập nhật nào cả.**

Dựa trên thư viện fbchat-muqit:
[https://github.com/togashigreat/fbchat-muqit](https://github.com/togashigreat/fbchat-muqit)

---

## 🚀 Cách hoạt động

* `main.py`
  Khởi động bot, cấu hình logging sạch, đăng ký handler.

* `handler/handler_commands.py`
  Chỉ có 1 router duy nhất:

  * Log mọi tin nhắn
  * Xử lý lệnh có prefix `/`, `!`, `.`
  * Gọi đúng module command
  * Nếu không có prefix → gọi `on_message()` của từng module (nếu có)

* `commands/`
  Mỗi file `.py` là một command độc lập.

Không có gì phức tạp — code bạn viết là code bot chạy.

---

## 🧩 Tự viết command

Chỉ cần tạo file trong thư mục `commands/`.

Ví dụ:

```python
NAME = "hello"
ALIASES = ["hi"]

async def handle(client, message, args):
    await client.send_message(
        text="Xin chào!",
        thread_id=message.thread_id,
    )
```

### Tùy chọn: xử lý chat thường (không prefix)

```python
async def on_message(client, message):
    text = (message.text or "").lower()
    if text == "xin chao":
        await client.send_message(
            text="Chào bạn!",
            thread_id=message.thread_id,
        )
```

---

## 🧪 Ví dụ đơn giản

`commands/ping.py`:

```python
NAME = "ping"
ALIASES = ["p"]

async def handle(client, message, args):
    await client.send_message(
        text="pong!",
        thread_id=message.thread_id,
    )
```

Sử dụng:

```
/ping
/p
```

---

## ⚙️ Cú pháp prefix

Hỗ trợ:

```
/lenh
!lenh
.lenh
```

Ví dụ:

```
/echo hello bạn
→ args = ["hello", "bạn"]
```

---

## 🛑 Không có update

Đây **không phải** framework.
Không phải plugin loader.
Không có bản cập nhật tự động.

> **Muốn thêm gì → tự viết.
> Muốn bot thông minh → tự code.
> Muốn auto send hình → tự làm file command.**

Toàn bộ hệ thống được thiết kế để bạn tự mở rộng dễ dàng.

ps: sau này, chỉ có làm. chịu khó, cần cù thì bù siêng năng
chỉ có làm thì mới có ăn, không nàm mà đòi có ăn thì ăn đầu puồi, nhá. ăn cứt. ( này th tác giả thềm vào :vv )
---
