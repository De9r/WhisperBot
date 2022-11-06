from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
اهلا {}.
 مرحبا بك في {}
هذا البوت مخصص للهمس يمكنك الهمس في المجموعات والقنوات والخاص وأي مكان وأعتبر انت من افضل البوتات 
شمنتظر دز همسه!    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 ارسال همسة 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 رجوع 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 ارسال همسة 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("كيف استخدم البوت ❔", callback_data="help"),
            InlineKeyboardButton("🎪 حول البوت. 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("قناة البوت", url="https://t.me/cn_world")],
        [InlineKeyboardButton("Support Group", url="https://t.me/+hgvlZ5VUuSI2MWMy")],
    ]

    # Help Message
    HELP = """
فقط قم بكتابة يوزر البوت بعدها رسالتك واخيرايوزر الشخص او ايديه.
مثال:
`@BA9BOT احبك @jj8jjj8`
    """

    # About Message
    ABOUT = """
**معلومات حول البوت** 
لغة التطوير : بايثون 
المكتبة : بايروكرام
الفكرة : @nnbbot
    """
