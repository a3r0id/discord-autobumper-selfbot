from datetime import datetime
from random import choice
from glbls import *

class hashes:
    def uword():
        return str(choice(glbls.chars) + choice(glbls.chars) + choice(glbls.chars) + choice(glbls.chars) + choice(glbls.chars) + choice(glbls.chars) + choice(glbls.chars) + choice(glbls.chars))

def uptime():
    #Get timestamp when called.
    uptime = datetime.now() - glbls.timestart
    return str(int(round(uptime.total_seconds() / 60))) + " Minutes"
