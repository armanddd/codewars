import math

def make_readable(seconds):
    hours = seconds / 60 / 60
    
    minutes = seconds / 60 % 60
    
    seconds = seconds % 60
    
    hours = math.floor(float(hours))
    minutes = math.floor(float(minutes))
    seconds = math.floor(float(seconds))

    if hours < 10:
        hours = "0" + str(hours)
        
    if minutes < 10:
        minutes = "0" + str(minutes)
        
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)
