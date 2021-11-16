import pytz
import datetime

# Timezone defines


def PDT():
    tz = pytz.timezone('America/Los_Angeles')
    pdtime = datetime.datetime.now(tz)
    pdtout = pdtime.strftime("%H%M")
    return int(pdtout)


def UTC():
    dt = datetime.time(16, 0, 0, tzinfo=pytz.UTC)
    dtp = dt.strftime("%H:%M:%S")
    return(dtp)


def checktime():
    t = datetime.datetime.utcnow()
    current_time = datetime.datetime.time(t).strftime("%H:%M:%S")
    return(current_time)

# channel defines


def gen1_channel(client):
    return(client.get_channel(841047848295333918))


def gen2_channel(client):
    return(client.get_channel(870877538543616060))


def botcom_channel(client):
    return(client.get_channel(841047847713112081))

# def swamptime():


# Channel name swap = General 2 into Swamp
