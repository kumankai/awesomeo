import discord
from dotenv import load_dotenv
import os
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        Guild = client.get_guild(1090707735873605643)
        for member in Guild.members:
            if member.id != 1091178692593602560:
                responses.members.append(member.name)
        print(responses.members)

    @client.event
    async def on_message(message):
        if message.author.id == client.id:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_message_edit(before, after):
        if not before.pinned and after.pinned:
            print(after.id)

    client.run(TOKEN)
