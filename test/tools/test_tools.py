from unittest import TestCase
from pybricks.tools.__stub.__tools import wait


class TestTools(TestCase):
    def test_wait(self):
        self.assertIsNone(wait(0))
