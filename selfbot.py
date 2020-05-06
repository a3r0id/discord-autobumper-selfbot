import discord
import asyncio
from random import choice
from time import sleep
from sys import stdout

#INCLUDES
from botlogging import *
from functions import *
from glbls import glbls
    
client = discord.Client()

@client.event
async def on_ready():
    print('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))
    activity = discord.Activity(name=glbls.presence, type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    glbls.timestart = datetime.now()
    
@client.event 
async def on_message(message):
    #FILTER
    m = message
    c = m.content#.encode(stdout.encoding, errors='replace').decode("utf-8")
    ch = m.channel
    a = m.author

    #LOGGING DIALOG
    logging.dialog(cmd_info(m, client).to_string())

        
    if c.startswith(f"{glbls.prefix}help"):
        await ch.send(
"""
```diff
+ Protero Self-Bot
- By Aero :)

-[HELP]
+ Help Command: --help

-[SERVER BUMPING]
+ Start Session: --bump
+ End Session: --stop SESSION_ID
+ View Sessions: --sessions

-[UTILITIES]
+ Test Responsiveness: --test
+ Uptime: --uptime

-[FUN]
+ --spam <amount> <channel_id> <message>
+ --embed <amount> <channel_id> <message>
+ --dm_spam <amount> <user_id> <message>
+ --dm_embed <amount> <user_id> <message>
+ --pic_embed_channel <channel id> <img url>
+ --pic_embed_dm <user id> <img url>

```
"""
            )
        

    if c.startswith("--test"):
        await ch.send("OK")


    if c.startswith("--sessions"):
        str_out = str(glbls.bumpers)
        await ch.send(f"**Active Bumping Sessions**\n```diff\n{str_out}\n```")
        

    if c.startswith("--bump"):
        
        nonce = str(hashes.uword())

        glbls.bumpers[nonce] = [True, m.channel.id, m.guild.id, m.channel.name, m.guild.name, m.author, m.id, str(datetime.now()), 0, nonce]
  
        m = await ch.send("!d bump")
        glbls.bumpers[nonce][8] += 1 
        await asyncio.sleep(5)
        await m.edit(content=f"Hey {a}! Use `--stop {nonce}` to stop the session. Sleeping for `{str(glbls.timing)} Seconds`!")

        
        while True:
            try:
                check = glbls.bumpers[nonce]
            except:
                await ch.send("**Ok im done!**")
                break
                
            # +30 seconds just in case. 7230
            await asyncio.sleep(glbls.timing)
            
            m = await ch.send("!d bump")
            glbls.bumpers[nonce][8] += 1
            
            await asyncio.sleep(5)
            await m.edit(content=choice(glbls.random_remarks))
            

    if c.startswith("--stop"):
        try:
            arg = c.split()[1]
        except:
            await ch.send("Huh? I need a session id!")
            return

        finally:
            try:
                st = str(glbls.bumpers[arg])
                del glbls.bumpers[arg]
                await ch.send(f"Removed session: {st}!")
            except:
                await ch.send("Unknown session key :/")
                return
                
    if c.startswith(f"--uptime"):
        await ch.send(f"I have been active for {uptime()}!")
    
    if c.startswith(f"--link"):
        await ch.send("**Get my script here: **\n```css\n[https://github.com/aerobotpro/discord-autobumper-selfbot]\n```\n**BE SURE TO STAR THE GITHUB AND FOLLOW!\n**")


    if c.startswith(f"{glbls.prefix}spam"):
        try:
            amount = int(c.split()[1])
            channel = client.get_channel(int(c.split()[2]))
            msg = c.replace(f"{c.split()[0]} {c.split()[1]} {c.split()[2]} ", "")
        except Exception as f:
            logging.err(str(f) + "\n")

        count = 0
        while True:
            await channel.send(f"[{count} / {amount}]\n```\n" + msg + "\n```")
            count += 1
            if count >= amount:
                break
            


    if c.startswith(f"{glbls.prefix}embed"):
        try:
            amount = int(c.split()[1])
            channel = client.get_channel(int(c.split()[2]))
            msg = c.replace(f"{c.split()[0]} {c.split()[1]} {c.split()[2]} ", "")
        except Exception as f:
            logging.err(str(f) + "\n")

        count = 0
        while True:
            embed = discord.Embed(title=msg, description=f"{x + 1} / 5 / {count} / {amount}", url=None, color=0x8000ff)
            await channel.send("", embed = embed)
            count += 1
            if count >= amount:
                break
             


    if c.startswith(f"{glbls.prefix}dm_spam"):
        try:
            amount = int(c.split()[1])
            chann = client.get_user(int(c.split()[2]))
            msg = c.replace(f"{c.split()[0]} {c.split()[1]} {c.split()[2]} ", "")
        except Exception as f:
            logging.err(str(f) + "\n")

        count = 0
        while True:
            await chann.send(f"[{count} / {amount}]\n```\n" + msg + "\n```")
            count += 1
            if count >= amount:
                break
            


    if c.startswith(f"{glbls.prefix}dm_embed"):
        try:
            amount = int(c.split()[1])
            chan1 = client.get_user(int(c.split()[2]))
            msg = c.replace(f"{c.split()[0]} {c.split()[1]} {c.split()[2]} ", "")
        except Exception as f:
            logging.err(str(f) + "\n")

        count = 0
        while True:
            embed = discord.Embed(title=msg, description=f"{count} / {amount}", url=None, color=0x8000ff)
            await chan1.send("", embed = embed)
            count += 1
            if count >= amount:
                break
            
    if c.startswith(f"{glbls.prefix}pic_embed_channel"):
        try:
            chan2 = client.get_channel(int(c.split()[1]))
            url = c.split()[2]
        except Exception as f:
            logging.err(str(f) + "\n")

        embed = discord.Embed(title="~", description=f"~", url=None, color=0x8000ff)
        embed.set_image(url=url) 
        await chan2.send("", embed = embed)

    if c.startswith(f"{glbls.prefix}pic_embed_dm"):
        try:
            chan3 = client.get_user(int(c.split()[1]))
            url = c.split()[2]
        except Exception as f:
            logging.err(str(f) + "\n")

        embed = discord.Embed(title="~", description=f"~", url=None, color=0x8000ff)
        embed.set_image(url=url) 
        await chan3.send("", embed = embed)        

            
client.run(glbls.TOKEN, bot=False)    
