import six
from io import open
import os
import time
import signal
import datetime

def log(msg):
    with open("app.log", "a", encoding="utf-8") as output:
        six.print_(six.u(str(msg)), file=output)

def main(config):
    global stop
    stop = False
    def on_exit(sig, frame):
        global stop
        stop = True
        log("got exit signal...")
    signal.signal(signal.SIGTERM, on_exit)
    while not stop:
        log(datetime.datetime.now())
        time.sleep(1)
