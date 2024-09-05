import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "24394477"))
API_HASH = os.getenv("API_HASH", "b7bf7b4ddaf7c8f81c9e7575ad7a2ac1")
SESSION = os.getenv("SESSION", "BQF0Ou0AlTv40ZRknTwKWjscETRWPQKVJAbGPbYwxd5wYxgQxu1xK-SxiU4uowvbOsowwSCwo-QRNwym4K15988xtcq6cc3C9Sn1PPPLr92xQvX0B4W73sQMYkmzicZQQx19SEkFlUTQgDdeTh7JGfAW48cpmzzEEGwDgMyi_heJt014Eub1j6inwxJRXzDFyW-RK_T0W6MUvBmdOccnLu7EGfh3MkWWlK4izJAef_-PJ31eH9m2xmmkdvvXlcGn_HpfUR0s3wCJ0My1rYmzOGBzEGPRDBZg4I0yowUgP9nb4FXqw0vY71sPpQvB9whfE8bP5bsS03C1ZBRchFj2L_APvnqAfQAAAAGWSmGJAA")
HNDLR = os.getenv("HNDLR", "+")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", " 5516578116").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client("Abhishek", API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
