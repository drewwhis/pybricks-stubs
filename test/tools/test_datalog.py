from unittest import TestCase
from pybricks.tools.__stub.__datalog import DataLog


class TestDataLog(TestCase):
    def test_constructor(self):
        try:
            DataLog('a', 'b', 'c')
            DataLog('a', 'b', 'c', name='name')
            DataLog('a', 'b', 'c', timestamp=False)
            DataLog('a', 'b', 'c', extension='tst')
            DataLog('a', 'b', 'c', append=True)
        except:
            self.fail()

    def test_log(self):
        d = DataLog('a')
        self.assertIsNone(d.log('any'))
