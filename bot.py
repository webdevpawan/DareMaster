import os
from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from dotenv import load_dotenv
from scraper import get_truth_and_dare

load_dotenv()
api_id = os.environ['APP_ID']
api_hash = os.environ['API_HASH']
token = os.environ['BOT_TOKEN']

app = Client("app", api_id=api_id, api_hash=api_hash, bot_token=token)


@app.on_message(filters.command(['start', 'help']))
async def greet(client, message):
    await message.reply("Hello 🌺\nUse this bot in any chat by typing @DareMasterBot.")


@app.on_message(filters.command(['contact']))
async def contact(client, message):
    await message.reply(
        "Hello DareMaster players! For help or custom dares, chat with @shoto_dx. Thanks for playing!"
    )


@app.on_inline_query()
async def answer(client, inline_query):
    truth, dare = await get_truth_and_dare()

    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Truth",
                input_message_content=InputTextMessageContent(truth),
            ),
            InlineQueryResultArticle(
                title="Dare",
                input_message_content=InputTextMessageContent(dare),
            )
        ],
        cache_time=1
    )


app.run()
