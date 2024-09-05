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
SESSION = os.getenv("SESSION", "BQBBs5QS0Togf5qgUBihHhVoMbsuGZ5qDkMrR9PDSR5hfN2z7LS138SQoPHVokP4E6kZRnO3VO49ADnky1D9QTn1g1renKLHQj56JUv-2aHqUAtQyM70gcofRvgD3XdAyf0K1kpc8Q1nFwzlUvwgdB34H-CAOQPIRnPYsXbmk4m6jikDd26Ev_SRgR1HGVZ7X8Amg-kp2nLsdlXAXlLFOQnweJKZntkGwgCGo5IRSgovo8jACHMg8fSRhzt0E_ALITQB1zWYq0hgHcGTLY6jDOYK4G2HMA-RZqsk_A8gFxOBtNCH57ui9BISGvYRJckzHtV_1NXuX9Y-hMhhBrDIPsPzAAAAAZZKYYkA")
HNDLR = os.getenv("HNDLR", "+")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", " 5516578116").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
