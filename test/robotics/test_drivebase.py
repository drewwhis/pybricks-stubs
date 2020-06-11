from unittest import TestCase
from pybricks.robotics.__stub.__drivebase import DriveBase
from pybricks.__stub.__control import Control
from pybricks.parameters.__stub.__port import Port
from pybricks.ev3devices.__stub.__motor import Motor


class TestDriveBase(TestCase):
    def test_constructor(self):
        try:
            DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        except:
            self.fail()

    def test_controls(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsInstance(base.distance_control, Control)
        self.assertIsInstance(base.heading_control, Control)

    def test_straight(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsNone(base.straight(0))

    def test_turn(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsNone(base.turn(0))

    def test_settings_no_return(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsNone(base.settings(0))
        self.assertIsNone(base.settings(0, 0))
        self.assertIsNone(base.settings(0, 0, 0))
        self.assertIsNone(base.settings(0, 0, 0, 0))

    def test_settings_return(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        result = base.settings()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertIsInstance(result[3], int)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 0)

    def test_drive(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsNone(base.drive(0, 0))

    def test_stop(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsNone(base.stop())

    def test_distance(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        result = base.distance()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_angle(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        result = base.angle()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_state(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        result = base.state()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertIsInstance(result[3], int)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 0)

    def test_reset(self):
        base = DriveBase(Motor(Port.A), Motor(Port.B), 0, 0)
        self.assertIsNone(base.reset())
