from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client("my_bot")  # Adjust with your bot name and configuration
call_py = PyTgCalls(bot)  # Pass the pyrogram client to PyTgCalls

async def main():
    try:
        print("STARTING UBOT CLIENT")
        await bot.start()
        print("STARTING PYTGCALLS CLIENT")
        await call_py.start()
        print(
            """
        ------------------------
       | MusicUserbot Activated! |
        ------------------------
"""
        )
        await idle()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("STOPPING USERBOT")
        await bot.stop()
