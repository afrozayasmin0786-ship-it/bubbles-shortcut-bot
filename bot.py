```python
import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

# ============================================================
# CONFIG
# ============================================================

GUILD_ID = 1543281300192895097
SOURCE_CHANNEL_ID = 1543291501939790036


# ============================================================
# ORIGINAL MESSAGE IDs
# ============================================================

SHORTCUTS = {

    "recruitbub": [
        1544037719892566076
    ],

    "promobub": [
        1544039984439500881
    ],

    "renewbub": [
        1544040741926346853
    ],

    "reminderbub": [
        1544040844355440771
    ],

    "dropbub": [
        1544040945933094963
    ],

    "waitlistedbub": [
        1544041155686174720
    ],

    "claimbub": [
        1544041336422928384
    ],

    "joinbub": [
        1544041437283229696
    ],

    "autobub": [
        1544041550420512818
    ],

    "byebub": [
        1544041686420815965
    ],

    "gpexpbub": [
        1544041932039389205
    ],

    "miss1bub": [
        1544042338878365808
    ],

    "miss2bub": [
        1544042441030500372
    ],

    "miss3bub": [
        1544042618596360212
    ],

    "miss4bub": [
        1544042690629468331
    ],

    "frozenbub": [
        1546882811435290774
    ],

    # LBbubs sends all five LB messages
    "LBbubs": [
        1546908840757428405,
        1546908871954661508,
        1546908898039177266,
        1546908927696965643,
        1546908937587134556
    ],
}


# ============================================================
# DISCORD BOT
# ============================================================

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = discord.Client(intents=intents)


# ============================================================
# SEND ORIGINAL MESSAGE
# ============================================================

async def send_original_message(channel, message_id):

    try:
        # Get the original banner channel.
        source_channel = bot.get_channel(SOURCE_CHANNEL_ID)

        if source_channel is None:
            source_channel = await bot.fetch_channel(
                SOURCE_CHANNEL_ID
            )

        # Fetch the actual original message.
        original = await source_channel.fetch_message(
            message_id
        )

        # ----------------------------------------------------
        # Copy the original message content.
        # ----------------------------------------------------

        content = original.content

        # ----------------------------------------------------
        # Copy attachments too, if the original has any.
        # ----------------------------------------------------

        files = []

        for attachment in original.attachments:
            try:
                file_bytes = await attachment.read()

                files.append(
                    discord.File(
                        fp=file_bytes,
                        filename=attachment.filename
                    )
                )

            except Exception as e:
                print(
                    f"Could not copy attachment "
                    f"{attachment.filename}: {e}"
                )

        # ----------------------------------------------------
        # Send copied message.
        # ----------------------------------------------------

        await channel.send(
            content=content if content else None,
            files=files,
            allowed_mentions=discord.AllowedMentions.none()
        )

        return True

    except discord.NotFound:
        print(
            f"Original message not found: {message_id}"
        )
        return False

    except discord.Forbidden:
        print(
            f"No permission to read original message: "
            f"{message_id}"
        )
        return False

    except discord.HTTPException as e:
        print(
            f"Discord error fetching message "
            f"{message_id}: {e}"
        )
        return False

    except Exception as e:
        print(
            f"Unexpected error for message "
            f"{message_id}: {type(e).__name__}: {e}"
        )
        return False


# ============================================================
# READY
# ============================================================

@bot.event
async def on_ready():

    print(
        f"Logged in as {bot.user}"
    )

    print(
        "🫧 Bubblezz shortcut bot is ready."
    )

    print(
        f"📚 Source channel: {SOURCE_CHANNEL_ID}"
    )

    print(
        f"🎀 Shortcuts loaded: {len(SHORTCUTS)}"
    )


# ============================================================
# MESSAGE HANDLER
# ============================================================

@bot.event
async def on_message(message):

    # Ignore bots.
    if message.author.bot:
        return

    # Only operate inside the Bubblezz server.
    if message.guild is None:
        return

    if message.guild.id != GUILD_ID:
        return

    # Read exactly what the user typed.
    shortcut = message.content.strip()

    # Check whether it is one of our shortcuts.
    if shortcut not in SHORTCUTS:
        return

    print(
        f"🫧 Shortcut used: {shortcut} "
        f"by {message.author}"
    )

    # --------------------------------------------------------
    # Fetch and resend each original message.
    # --------------------------------------------------------

    success = True

    for message_id in SHORTCUTS[shortcut]:

        result = await send_original_message(
            message.channel,
            message_id
        )

        if not result:
            success = False

    # --------------------------------------------------------
    # Delete the shortcut message after successful output.
    # --------------------------------------------------------

    if success:

        try:
            await message.delete()

            print(
                f"🗑️ Deleted shortcut: {shortcut}"
            )

        except discord.Forbidden:
            print(
                "⚠️ Cannot delete shortcut message."
            )

        except discord.HTTPException as e:
            print(
                f"⚠️ Could not delete shortcut: {e}"
            )


# ============================================================
# START
# ============================================================

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN is missing from Railway Variables."
    )

bot.run(TOKEN)
```
