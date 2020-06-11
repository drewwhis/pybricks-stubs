from unittest import TestCase
from pybricks.tools.__stub.__stopwatch import StopWatch


class TestStopWatch(TestCase):
    def test_time(self):
        s = StopWatch()
        result = s.time()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_pause(self):
        s = StopWatch()
        self.assertIsNone(s.pause())

    def test_resume(self):
        s = StopWatch()
        self.assertIsNone(s.resume())

    def test_reset(self):
        s = StopWatch()
        self.assertIsNone(s.reset())
