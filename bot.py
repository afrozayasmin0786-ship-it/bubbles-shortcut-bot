import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = 1543281300192895097
SOURCE_CHANNEL_ID = 1543291501939790036


SHORTCUTS = {
    "recruitbub": [1544037719892566076],
    "promobub": [1544039984439500881],
    "renewbub": [1544040741926346853],
    "reminderbub": [1544040844355440771],
    "dropbub": [1544040945933094963],
    "waitlistedbub": [1544041155686174720],
    "claimbub": [1544041336422928384],
    "joinbub": [1544041437283229696],
    "autobub": [1544041550420512818],
    "byebub": [1544041686420815965],
    "gpexpbub": [1544041932039389205],
    "miss1bub": [1544042338878365808],
    "miss2bub": [1544042441030500372],
    "miss3bub": [1544042618596360212],
    "miss4bub": [1544042690629468331],
    "frozenbub": [1546882811435290774],

    "LBbubs": [
        1546908840757428405,
        1546908871954661508,
        1546908898039177266,
        1546908927696965643,
        1546908937587134556
    ],
}


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = discord.Client(intents=intents)


async def send_original_message(destination, message_id):

    try:
        # Fetch the source channel directly from Discord.
        source_channel = await bot.fetch_channel(
            SOURCE_CHANNEL_ID
        )

        print(
            f"📚 Source channel loaded: "
            f"{source_channel.name}"
        )

        # Check the bot's effective permissions.
        permissions = source_channel.permissions_for(
            source_channel.guild.me
        )

        print(
            f"🔐 View Channel: {permissions.view_channel}"
        )

        print(
            f"🔐 Read Message History: "
            f"{permissions.read_message_history}"
        )

        # Fetch the original banner.
        original = await source_channel.fetch_message(
            message_id
        )

        print(
            f"✅ Found original message: {message_id}"
        )

        # Copy the original content.
        content = original.content

        # Copy attachments if there are any.
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
                    f"⚠️ Could not copy attachment "
                    f"{attachment.filename}: {e}"
                )

        # Send the copied message.
        await destination.send(
            content=content if content else None,
            files=files,
            allowed_mentions=discord.AllowedMentions.none()
        )

        print(
            f"🫧 Sent banner from {message_id}"
        )

        return True

    except discord.Forbidden:

        print(
            f"❌ Discord denied access to "
            f"message {message_id}"
        )

        return False

    except discord.NotFound:

        print(
            f"❌ Message {message_id} was not found."
        )

        return False

    except discord.HTTPException as e:

        print(
            f"❌ Discord HTTP error: {e}"
        )

        return False

    except Exception as e:

        print(
            f"❌ Unexpected error: "
            f"{type(e).__name__}: {e}"
        )

        return False


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


@bot.event
async def on_message(message):

    if message.author.bot:
        return

    if message.guild is None:
        return

    if message.guild.id != GUILD_ID:
        return

    shortcut = message.content.strip().lower()

    if shortcut not in SHORTCUTS:
        return

    print(
        f"🫧 Shortcut used: "
        f"{shortcut} by {message.author}"
    )

    success = True

    for message_id in SHORTCUTS[shortcut]:

        result = await send_original_message(
            message.channel,
            message_id
        )

        if not result:
            success = False

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


if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN is missing from Railway Variables."
    )

bot.run(TOKEN)
