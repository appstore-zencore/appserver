import os
import time
import unittest
from zdas import load_pid
from zdas import is_running


class TestZas(unittest.TestCase):

    def test01(self):
        os.system("zas -c app.yaml start")
        time.sleep(2)
        pid = load_pid("app.pid")
        assert pid
        assert pid != os.getpid()
        assert is_running(pid)
        print(pid)
        print(os.getpid())
        os.system("zas -c app.yaml stop")
        time.sleep(2)
        assert not is_running(pid)
