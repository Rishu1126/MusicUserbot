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
SESSION = os.getenv("SESSION", "BQF0Ou0AapipsHULYsraEZnhODKmR7kSkZaKWuYXHaqSOTIawyd4kt6yB9OjdjKUqXlOMXXR9YW9v9B7gfve48lznfO9ZB1SaOUyPDVH1pyFTz7ezR1ZQbzPe6_CJ2pg7f8Fe1IvkmgLiJBNoA7lBJiQEJnR5EfwXZBD6KN4uqq20z3pwAlNLUyhuYFaRUjdmTO4pZR1wcKsKw1jUElvWH2SRPOel0QHfIEl31nX7SwaFdUyQkkxTS8AEoc1G0t1D9pHecj8nhMekMhcgqGAHDMUN3MqWH0xt2_s24AhqsSelsMDu6VsUGz3nBJx2tM5iZJGUEEdIJmzZIX2CYV3IjOSIbbTmgAAAAGWSmGJAA")
HNDLR = os.getenv("HNDLR", "+", "!")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", " 5516578116").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
