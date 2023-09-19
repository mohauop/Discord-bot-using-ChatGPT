import discord
#import torch
from discord.ext import commands
import openai


















#Bot




async def send_messages(message, user_message, is_private):
    try:
        response = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    Token = "MTE0ODQwMTI0OTEyNTkyNDk5Ng.G17KZL.Wqsh_IkpTUoIjBSMc_as4C-7H6ZoU1Y2G6xYyA"
    client = discord.Client(intents=discord.Intents.default())

    @client.event 
    async def on_ready():
        print(f'{client.user} is now running !')





    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said : '{user_message}' ({channel})")



        await send_messages(message, user_message,is_private=True)
        #else:
         #   await send_messages(message, user_message,is_private=False)
    client.run(Token)

#responses


openai_key = "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"
openai_org = "org-fyt0wgXh3zouAeX3qUpjbZst"

# Retrieve Enviornment Variables
openai.organization = openai_org
openai.api_key = openai_key






def handle_response(message): #-> str:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message
    )
    message_text = response["choices"][0]["message"]["content"]
    return message_text








#Main
if __name__ == '__main__':
    run_discord_bot()