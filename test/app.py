import os
import time
import signal
import datetime

def main(config):
    global stop
    stop = False
    def on_exit(sig, frame):
        global stop
        stop = True
    signal.signal(signal.SIGTERM, on_exit)
    while not stop:
        with open("app.log", "a", encoding="utf-8") as output:
            print(str(datetime.datetime.now()), file=output)
        time.sleep(1)
