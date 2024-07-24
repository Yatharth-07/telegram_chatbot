def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I am your bot.')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

# You can add more command handlers here