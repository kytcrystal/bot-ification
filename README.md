# bot-ification

A fun personal project to create a Telegram bot.
This bot sends notifications on the number of GitHub commits needed to create the desired GitHub contribution graph.


## Get Started

Ensure that [Python](https://www.python.org/downloads/) is already installed with version 3.8 or later.

Install [Poetry](https://python-poetry.org/docs/), a tool for dependency management and packaging in Python.

Environment File

- Create a file name `.env`
- Inside the file, include `export BOT_TOKEN=<your_token>`. In `your_token`, replace with the token from Telegram. Instructions on how to get the token can be found [here](#get-telegram-bot-token)

To run bot.py

- Load environment file, run `source .env`
- Run file in virtual environment `poetry run python3 bot.py`

## Get Telegram Bot Token

In Telegram, search for [`@BotFather`](https://t.me/BotFather)

Start the conversation with the bot using `/start`

Create a new bot using `/newbot`

Provide a name and username for your bot. With this step, you should receive your token that should be stored safely.


## References

- [Telegram Docs](https://core.telegram.org/bots/tutorial)
- [Telegram Bot Reference Tutorial](https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/tree/main)
