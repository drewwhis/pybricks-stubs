from unittest import TestCase
from pybricks.__stub.__control import Control


class TestControl(TestCase):
    def test_scale_is_float(self):
        control = Control()
        self.assertIsInstance(control.scale, float)

    def test_done(self):
        control = Control()
        result = control.done()
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_stalled(self):
        control = Control()
        result = control.stalled()
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_limits_no_return(self):
        control = Control()

        result = control.limits(0)
        self.assertIsNone(result)

        result = control.limits(0, 0)
        self.assertIsNone(result)

        result = control.limits(0, 0, 0)
        self.assertIsNone(result)

    def test_limits_return(self):
        control = Control()

        result = control.limits()
        self.assertIsInstance(result, tuple)
        self.assertEqual(3, len(result))
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])
        self.assertEqual(0, result[2])

    def test_pid_no_return(self):
        control = Control()

        result = control.pid(0)
        self.assertIsNone(result)

        result = control.pid(0, 0)
        self.assertIsNone(result)

        result = control.pid(0, 0, 0)
        self.assertIsNone(result)

        result = control.pid(0, 0, 0, 0)
        self.assertIsNone(result)

        result = control.pid(0, 0, 0, 0, 0)
        self.assertIsNone(result)

        result = control.pid(0, 0, 0, 0, 0, 0)
        self.assertIsNone(result)

    def test_pid_return(self):
        control = Control()

        result = control.pid()
        self.assertIsInstance(result, tuple)
        self.assertEqual(6, len(result))
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertIsInstance(result[3], int)
        self.assertIsInstance(result[4], int)
        self.assertIsInstance(result[5], int)
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])
        self.assertEqual(0, result[2])
        self.assertEqual(0, result[3])
        self.assertEqual(0, result[4])
        self.assertEqual(0, result[5])

    def test_target_tolerances_no_return(self):
        control=Control()

        result=control.target_tolerances(0)
        self.assertIsNone(result)

        result=control.target_tolerances(0, 0)
        self.assertIsNone(result)

    def test_target_tolerances_return(self):
        control=Control()

        result=control.target_tolerances()
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

    def test_stall_tolerances_no_return(self):
        control=Control()

        result=control.stall_tolerances(0)
        self.assertIsNone(result)

        result=control.stall_tolerances(0, 0)
        self.assertIsNone(result)

    def test_stall_tolerances_return(self):
        control=Control()

        result=control.stall_tolerances()
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])
