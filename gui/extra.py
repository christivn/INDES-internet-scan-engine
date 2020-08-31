import datetime

def time():
    date = datetime.datetime.now()
    return str(date.hour)+":"+str(date.minute)
    