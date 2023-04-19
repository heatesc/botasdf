from collections import deque
import os
import discord
from discord.ext import commands
from discord import Intents
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')
bot = discord.Bot()
guild_id = 983349060020875264
test_bot = discord.Bot(debug_guilds=[guild_id])
message_memory = 1000

previous_messages = deque(maxlen=message_memory)
# reads in the contents of ./bot_init.txt and stores in 'bot_init'
bot_init = open('./bot_init.txt', 'r').read()


@bot.command(description="say sth")
async def chat(ctx, text):
    print("chat command run")

    # Add the new message to the deque
    author_name = str.split(str(ctx.author), '#')[0]
    previous_messages.append(
        {'role': 'user', 'name': author_name, 'content': text})

    # Build the messages list for the API call, including the system message and the last 1000 previous messages
    messages = [{'role': 'user',
                 'content': bot_init}]
    messages.extend(previous_messages)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=300
    )

    # Extract the answer from the API response
    answer = response['choices'][0]['message']['content']
    # print(response)
    # Send the answer back to the user
    prefix = f"\n**{author_name}'s input**\n" + \
        text + "\n" + "\n**My response**\n"
    await ctx.send(prefix+str(answer)+"\n")
    print(prefix + str(answer) + "\n")

bot.run(os.environ.get('DISCORD_TOKEN'))
