import logging
import os
from datetime import date
import csv

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes

logger = logging.getLogger(__name__)

# Store bot screaming status
screaming = False

# Pre-assign menu text
FIRST_MENU = "<b>Menu 1</b>\n\nCheck if commit is needed."
SECOND_MENU = "<b>Menu 2</b>\n\nCheck how many commits needed."

# Pre-assign button text
CHECK_BUTTON = "Commit Today?"
BACK_BUTTON = "Back"
GITHUB_LINK = "GitHub"

TOKEN = os.environ.get("BOT_TOKEN")
if TOKEN == None:
    raise Exception("Please set bot token")

async def checktoday(update: Update, context: CallbackContext) -> None:

    today = date.today()
    commit_number = get_commit_number(today)

    await update.message.reply_text(
        text=f"Today is {today}. You should make {commit_number} commits today"
    )

def get_commit_number(input_date) -> None:

    csv_file = 'commit_dates.csv'
    commit_dict = csv.DictReader(open(csv_file))

    commit_number = "0"
    for row in commit_dict:
        if row["date"] == str(input_date):
            print(row["date"], row["number of commits"])
            commit_number = row["number of commits"]

    return commit_number

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Hi! Use /checktoday to check if commit is needed today :)")

def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("checktoday", checktoday))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()