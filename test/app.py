import os
import time
import datetime

def main(config):
    global stop
    stop = False
    while not stop:
        with open("app.log", "a", encoding="utf-8") as output:
            print(str(datetime.datetime.now()), file=output)
        time.sleep(1)

