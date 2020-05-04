import discord
import asyncio
from datetime import datetime

TOKEN = open("token.txt")

#Crypto
from random import choice
chars = ['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']
random_remarks = ["Ayoo!", "Whats poppin?!", "Hey all you cool cats and kittens!", "Oye Matey!"]
class hashes:
    global chars
    def uword():
        return str(choice(chars) + choice(chars) + choice(chars) + choice(chars) + choice(chars) + choice(chars) + choice(chars) + choice(chars))   

class glbls:
    bumpers = {}
    timing = 7230
    timestart = None

def uptime():
    #Get timestamp when called.
    uptime = datetime.now() - glbls.timestart
    return str(int(round(uptime.total_seconds() / 60))) + " Minutes"            

client = discord.Client()

@client.event
async def on_ready():
    print('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))
    activity = discord.Activity(name='Netflix', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    glbls.timestart = datetime.now()
    
   

@client.event 
async def on_message(message):
    m = message
    c = m.content
    ch = m.channel
    a = m.author

    if c.startswith("--help"):
        await ch.send(
"""
```diff
+ Hey I'm here to bump your server!
- I'm not a self bot or anything!

Help Command: --help

Start Session: --bump

End Session: --stop SESSION_ID

Test Responsiveness: --test

Uptime: --uptime
```
"""
            )

    if c.startswith("--test"):
        await ch.send("OK")

    if c.startswith("--bump"):
        
        nonce = str(hashes.uword())
        
        m = await ch.send("!d bump")
        await asyncio.sleep(5)
        await m.edit(content=f"Hey {a}! Use `--stop {nonce}` to stop the session. Sleeping for `{str(glbls.timing)} Seconds`!")

        glbls.bumpers[nonce] = True
        
        while True:
            try:
                check = glbls.bumpers[nonce]
            except:
                await ch.send("**Ok im done!**")
                break
                
            # +30 seconds just in case. 7230
            await asyncio.sleep(glbls.timing)
            
            m = await ch.send("!d bump")
            await asyncio.sleep(5)
            await m.edit(content=choice(random_remarks))    

    if c.startswith("--stop"):
        try:
            arg = c.split()[1]
        except:
            await c.send("Huh? I need a session id!")
            return

        finally:
            try:
                del glbls.bumpers[arg]
            except:
                await c.send("Unknown session key :/")
                return
                
    if c.startswith(f"--uptime"):
        await ch.send(f"I have been active for {uptime()}!")
        

client.run(TOKEN, bot=False)    
