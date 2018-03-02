import os
import time
import signal
import threading
import multiprocessing
import unittest
from zdas import load_pid
from zdas import is_running


def system_nowait(cmd):
    t = multiprocessing.Process(target=os.system, args=[cmd], daemon=True)
    t.start()


class TestZas(unittest.TestCase):

    def test01(self):
        system_nowait("zas -c test01.yaml start")
        time.sleep(2)
        pid = load_pid("test01.pid")
        assert pid
        assert pid != os.getpid()
        assert is_running(pid)
        print(pid)
        print(os.getpid())
        system_nowait("zas -c test01.yaml stop")
        time.sleep(2)
        assert not is_running(pid)

    def test02(self):
        handler = signal.signal(signal.SIGTERM, signal.SIG_IGN)
        system_nowait("zas -c test02.yaml start")
        time.sleep(2)
        signal.signal(signal.SIGTERM, handler)

        pid = load_pid("test02.pid")
        assert pid
        assert pid != os.getpid()
        assert is_running(pid)

        print(pid)
        print(os.getpid())
        system_nowait("zas -c test02.yaml stop")
        time.sleep(4)
        assert not is_running(pid)
