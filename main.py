import discord
from llm import answer_query

from Observability_metrics import QUERY_TIME, QUERY_COUNT, start_metrics_server
start_metrics_server()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#Nexus'):
        response = answer_query(message.content)
        await message.channel.send(response)


client.run('Your_bot_token') # Enter the bot token here
