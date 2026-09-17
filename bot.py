import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


RESPONSES = {

    "recruitbub": """ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖  [🐈](https://discord.com/assets/ff0e6e37f1e9e686.svg)↝65ᴘ           [🐕](https://discord.com/assets/21f5a5ed99c27d76.svg)↝75ᴘ [🍱](https://discord.com/assets/20edff0f83748ae5.svg)↝16ᴘ         4[🍱](https://discord.com/assets/20edff0f83748ae5.svg)↝65ᴘ ʙʀᴇᴀᴋ✘ • sғᴡ✓ • ᴅɴs✘""",

    "promobub": """ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖   1[🍱](https://discord.com/assets/20edff0f83748ae5.svg)⋆18ᴘ     5[🍱](https://discord.com/assets/20edff0f83748ae5.svg)⋆90ᴘ  4[🍱](https://discord.com/assets/20edff0f83748ae5.svg)⋆70ᴘ   10[🍱](https://discord.com/assets/20edff0f83748ae5.svg)⋆180ᴘ ˖•─── ʙᴇɴᴛᴏ ᴘʀᴏᴍᴏ☁︎""",

    "renewbub": """☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖ ᴜʀ ʙᴜʙʙʟᴇs ʀ ʙᴜʀsᴛɪɴɢ ☾ 20 ᴘ ʟᴇꜰᴛ ☽[🐈](https://discord.com/assets/ff0e6e37f1e9e686.svg)⋆[🐶](https://discord.com/assets/63eeb1be5a56dd59.svg)⋆[🍱](https://discord.com/assets/20edff0f83748ae5.svg)""",

    "reminderbub": """𓈒𓏸 𐦖˖ ᴅʀᴏᴘ ɪɴ 14 ᴍɪɴs ᴛʜᴇ ʙᴜʙʙʟᴇs ᴀʀᴇ ʀɪsɪɴɢ ⋆. ̊ ☾⭒. ̊ᴋᴇᴇᴘ ᴡᴀᴛᴄʜ ⋆""",

    "dropbub": """≽^• ˕ • ྀི≼ ᴅʀᴏᴘ ᴛɪᴍᴇ""",

    "waitlistedbub": """ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖 ˖ ☾ ᴡᴀɪᴛʟɪsᴛᴇᴅ⊹1[🐱](https://discord.com/assets/80d98aa027a3ee75.svg) ⌇""",

    "claimbub": """☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖ • ᴀᴠᴀɪʟᴀʙʟᴇ sᴘᴏᴛ [🐱](https://discord.com/assets/80d98aa027a3ee75.svg)[🐶](https://discord.com/assets/63eeb1be5a56dd59.svg)[🍱](https://discord.com/assets/20edff0f83748ae5.svg)
ᴡᴀʟʟ ʙᴀᴄᴋ ᴛᴏ ᴄʟᴀɪᴍ ғɪʀsᴛ ᴄᴏᴍᴇ, ғɪʀsᴛ sᴇʀᴠᴇ""",

    "joinbub": """݁☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖ • ɪɴᴠɪᴛᴇᴅ, ᴊᴏɪɴ ɪɴ 2 ʜᴏᴜʀs ᴏʀ ʟᴏsᴇ ʏᴏᴜʀ sᴘᴏᴛ𖦹°⭒˚｡""",

    "autobub": """☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖ • ᴀᴜᴛᴏ-ʀᴇɴᴇᴡᴇᴅ〔0/4[🐱](https://discord.com/assets/80d98aa027a3ee75.svg)〕 ᴀsᴋ ᴀᴅᴍɪɴ ᴛᴏ ʟɪɴᴇ ᴜᴘ ˖• ───ᴜʀ ʙᴜʙ's sᴀғᴇ ☁︎""",

    "byebub": """☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖ • ɴᴜᴜ! ᴜʀ ʙᴜʙʙʟᴇ ᴘᴏᴘᴘᴇᴅ ⋆｡𖦹°⭒˚｡⋆sᴇᴇ ᴜ sᴏᴏɴ ☁︎""",

    "gpexpbub": """☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ 𐦖˖ • ɢᴘ ɪs ᴇxᴘɪʀɪɴɢ sᴏᴏɴ ʀᴇɴᴇᴡɪɴɢ?〔[🍱](https://discord.com/assets/20edff0f83748ae5.svg)/ᴡᴇᴇᴋ〕 ˖•───ᴅᴏɴ'ᴛ ᴅʀɪғᴛ ᴀᴡᴀʏ""",

    "miss1bub": """βׁ υׁ βׁ βׁ ᥣׁ ꫀׁ ꯱ׁ ⇀1sᴛ ᴍɪss ⋆𐦖 ᴍɪssᴇᴅ ᴀ ʙᴜʙʙʟᴇ? ɪᴛ ʜᴀᴘᴘᴇɴs. [🫧](https://discord.com/assets/d4e0b5c9c8d1679c.svg) ⇢ ɴᴇxᴛ ᴏɴ ᴄᴀ ࣪ ִֶָ☾.""",

    "miss2bub": """βׁ υׁ βׁ βׁ ᥣׁ ꫀׁ ꯱ׁ ⇀ 2ɴᴅ ᴍɪss ⋆𐦖 ᴀɴᴏᴛʜᴇʀ ʙᴜʙʙʟᴇ ɢᴏɴᴇ! ᴜʜ-ᴏʜ [🪸](https://discord.com/assets/d3716a5025089169.svg)⇢ ɪᴛ's sʟᴇᴇᴘʏ ᴛɪᴍᴇ ࣪ ִֶָ☾.""",

    "miss3bub": """βׁ υׁ βׁ βׁ ᥣׁ ꫀׁ ꯱ׁ ⇀ 𝟹ʀᴅ ᴍɪss ⋆𐦖 ᴄᴏɴsɪᴅᴇʀ ʙᴜʙʙʟᴇ ᴡʀᴀᴘᴘɪɴɢ ɪᴛ [🌨️](https://discord.com/assets/d84d24696a9d5195.svg)⇢ ᴇɴᴅ ᴏғ ʟɪɴᴇᴜᴘ ࣪ ִֶָ☾.""",

    "miss4bub": """βׁ υׁ βׁ βׁ ᥣׁ ꫀׁ ꯱ׁ ⇀ 𝟺ᴛʜ ᴍɪss ⋆𐦖 ᴘᴏᴘᴘᴇᴅ ʏᴏᴜʀ ᴡᴀʏ ɪɴᴛᴏ ᴛʀᴏᴜʙʟᴇ [🦭](https://discord.com/assets/0de2cbb95090de5d.svg)⇢ ᴛʜᴀᴛ's -𝟻 ʙᴜʙs ࣪ ִֶָ☾.""",

    "frozenbub": """݁☁︎ ϐׁ  υׁ  ϐׁ  ϐׁ  ᥣׁ  ꫀׁ  ꯱ׁ  𐦖˖ •        ⟢ 200 ᴘ ʟᴇꜰᴛ ❆      ᴇɴᴅs ᴏɴ「ᴍᴍ/ᴅᴅ」ˎˊ˗ ─── ғʀᴏᴢᴇɴ ʙᴜʙʙʟᴇ 𖥔˚❆""",

    "LBbubs": """𝟤.𝟢 . ⊹ ࣪ ˖⟡ ◦ ᗷᑘᗷᗷᒪᘿS ˎˊ˗

𝟣.𝟧 . ⊹ ࣪ ˖⟡ ◦ ᗷᑘᗷᗷᒪᘿS ˎˊ˗

ʟ ʙ . ⊹ ࣪ ˖⟡ ◦ ᗷᑘᗷᗷᒪᘿS ˎˊ˗

𝟢.𝟧 . ⊹ ࣪ ˖⟡ ◦ ᗷᑘᗷᗷᒪᘿS ˎˊ˗

ᴅᴇᴅ. ⊹ ࣪ ˖⟡ ◦ ᗷᑘᗷᗷᒪᘿS ˎˊ˗"""
}


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    shortcut = message.content.strip()

    if shortcut in RESPONSES:
        await message.channel.send(RESPONSES[shortcut])


if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing from Railway Variables.")

bot.run(TOKEN)
