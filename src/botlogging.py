import discord
from datetime import datetime
from glbls import *

#Const logging utils
def log(inp, fname):
    with open(fname, "a" , encoding="utf-8") as D:
        D.write(inp)
        
class logging:
    def err(inp): log(inp, "logs/errors.txt")
    def sys(inp): log(inp, "logs/system.txt")
    def dialog(inp): log(inp, "logs/dialog.txt")

class cmd_info:
    def __init__(self, m, client):
        self.m = m
        
        if m.channel.type == discord.DMChannel:
            print("DM CHANNEL")
            
            
        self.special_meta_flags = ""

        if glbls.prefix in m.content:
            self.special_meta_flags += "> IS COMMAND\n"
            
            
        
        if m.author == client.user:
            self.special_meta_flags += "> IS ME\n"
            
        if m.author.bot:
            self.special_meta_flags += "> IS BOT\n"

        start_date = str(discord.utils.snowflake_time(m.author.id))
        start_date_day = start_date.split(" ")[0]

        if str(datetime.now().date()) == start_date_day:
            self.special_meta_flags += "> ACCOUNT CREATED TODAY\n"
        else:
            self.special_meta_flags += f"> ACCOUNT CREATED: {start_date_day}\n"
                    
        try:
            webhk = m.webhook_id
            self.special_meta_flags += f"> IS WEBHOOK: {webhk}\n"
        except: pass
        
        #if m.flags.urgent:
        #    self.special_meta_flags += "> IS FROM DISCORD TRUST & SAFETY!\n"

        self.special_meta_flags += f"> Type: {m.type}\n"
        
            
    def to_string(self):
        try:
            stuff = f"""
Content:

{self.m.content} | {self.m.id}

User: {self.m.author} | {self.m.author.id}
Channel: {self.m.channel} | {self.m.channel.id}
Guild: {self.m.guild} | {self.m.guild.id}
Other Info [Flags]:
{self.special_meta_flags}
"""
            #IF ABOVE FAILS THEN ITS A DM.
        except Exception as dd:
            stuff = f"""
Content:

{self.m.content} | {self.m.id}

User: {self.m.author} | {self.m.author.id}
Channel: {self.m.channel} | {self.m.channel.id}
Guild: Direct Message
Other Info [Flags]:
{self.special_meta_flags}
"""    
        return stuff
