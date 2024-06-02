# bot-ification

A fun personal project to create a Telegram bot.
This bot sends notifications on the number of GitHub commits needed to create the desired GitHub contribution graph.


## Get Started
Ensure that [Python](https://www.python.org/downloads/) is already installed with version 3.8 or later.

Install [Poetry](https://python-poetry.org/docs/), a tool for dependency management and packaging in Python.

Environment File
- Create a file name `.env`
- Inside the file, include `export BOT_TOKEN=<token>`

To run bot.py
  - Reload environment file, run `source .env`
  - Run file in virtual environment `poetry run python3 bot.py`


Reference:
- https://core.telegram.org/bots/tutorial
- https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/tree/main