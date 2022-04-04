import discord
import random
import requests
import json
from keep_alive import keep_alive

TOKEN = 'OTIyODY4ODE4ODMxOTAwNzEz.YcHukA.wqN2LdNP09hiMD_IN_JC1U7bcFw'

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    msg = message.content

    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == 'discord-bot-tutorial':
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"See you later {username}!")
            return
        elif user_message.lower() == "!random":
            response = f"This is your random number: {random.randrange(1000000)}"
            await message.channel.send(response)

        elif any(word in msg for word in sad_words):
            await message.channel.send(random.choice(encouragements))

    if user_message.lower() == '!anywhere':
        await message.channel.send("This can be used everywhere")
        return

    # if message.content.startswith('!inspire'):
    #       quote = get_quote()
    #       await message.channel.send(quote)

    if user_message.lower() == '!inspire':
        quote = get_quote()
        await message.channel.send(quote)


keep_alive()
client.run(TOKEN)
