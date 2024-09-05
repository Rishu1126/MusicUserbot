import asyncio
from pytgcalls import idle
from config import call_py, bot

async def main():
    try:
        print("STARTING UBOT CLIENT")
        await bot.start()
        print("UBOT CLIENT STARTED")
        print("STARTING PYTGCALLS CLIENT")
        await call_py.start()
        print("PYTGCALLS CLIENT STARTED")
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
        print("USERBOT STOPPED")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
