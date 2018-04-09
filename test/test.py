
import six
import os
import time
import signal
import threading
import multiprocessing
import unittest
from daemon_application import load_pid
from daemon_application import is_running


def system_nowait(cmd):
    t = multiprocessing.Process(target=os.system, args=[cmd])
    t.start()


class TestAppserver(unittest.TestCase):

    def test01(self):
        system_nowait("appserver -c test01.yaml start")
        time.sleep(2)
        pid = load_pid("test01.pid")
        assert pid
        assert pid != os.getpid()
        assert is_running(pid)
        six.print_(pid)
        six.print_(os.getpid())
        system_nowait("appserver -c test01.yaml stop")
        time.sleep(2)
        assert not is_running(pid)

    def test02(self):
        handler = signal.signal(signal.SIGTERM, signal.SIG_IGN)
        system_nowait("appserver -c test02.yaml start")
        time.sleep(2)
        signal.signal(signal.SIGTERM, handler)

        pid = load_pid("test02.pid")
        assert pid
        assert pid != os.getpid()
        assert is_running(pid)

        six.print_(pid)
        six.print_(os.getpid())
        system_nowait("appserver -c test02.yaml stop")
        time.sleep(4)
        assert not is_running(pid)
