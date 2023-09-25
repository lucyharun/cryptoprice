import logging

from telegram import Update
from telegram.ext import (
    ContextTypes,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        parse_mode="markdown",
        text="Did you know, you can ask me for the current price of any crypto by typing:\n\n"
        "`/p <crypto_ticker>` \n\n"
        "For example, `/p btc` will give you the current price of Bitcoin. Enjoy!\n\n"
        "To display the complete list of price, type `/cmc <crypto_ticker>`"
        "Type `/help` to see all available command, some feature still on developing",
    )
    logging.info("Start call")


async def bot_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        parse_mode="markdown",
        disable_web_page_preview=True,
        text="*List of Commands:*\n\n"
        "`/p <crypto_symbol>` - to receive the current price and historical variation from CoinCecko\n"
        "`/c <crypto_symbol>` - to receive the chart in different timeframes of selected crypto\n"
        "`/cmc <crypto_symbol>` - to receive the current price and historical variation from CoinMarketCap\n"
        "`/chart_color` to select chart color theme\n"
        "/cmckey - to reveive info about CoinMarketCap api key usage"
        "/dom - to receive the top 10 most capitalized tokens\n"
        "/gas - to receive real time gas information on ERC\n"
        "/news - to receive CoinTelegraph news\n"
        "/help - to receive this message\n\n"
        "This bot is written with love by CypherBOT Team"
        "[Dev](https://t.me/asinpeda)\n\n"
        "`Bot version: 1.0.1`\n",
    )
    logging.info(f"Help call")
