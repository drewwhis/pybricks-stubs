from unittest import TestCase
from pybricks.ev3devices.__stub.__motor import Motor
from pybricks.parameters.__stub.__port import Port
from pybricks.parameters.__stub.__direction import Direction
from pybricks.parameters.__stub.__stop import Stop


class TestMotor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, Motor, Port.S1)
        self.assertRaises(ValueError, Motor, Port.S2)
        self.assertRaises(ValueError, Motor, Port.S3)
        self.assertRaises(ValueError, Motor, Port.S4)

        try:
            Motor(Port.A)
            Motor(Port.B)
            Motor(Port.C)
            Motor(Port.D)
        except:
            self.fail()

        try:
            Motor(Port.A, Direction.COUNTERCLOCKWISE, [1, 2])
            Motor(Port.A, Direction.COUNTERCLOCKWISE, [[1, 2], [2, 4]])
        except:
            self.fail()

    def test_speed(self):
        motor = Motor(Port.A)
        result = motor.speed()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_angle(self):
        motor = Motor(Port.A)
        result = motor.angle()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_reset_angle(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.reset_angle(100))

    def test_stop(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.stop())

    def test_brake(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.brake())

    def test_hold(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.hold())

    def test_run(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.run(100))

    def test_run_time(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.run_time(100, 100))
        self.assertIsNone(motor.run_time(100, 100, Stop.COAST))
        self.assertIsNone(motor.run_time(100, 100, Stop.COAST, False))

    def test_run_angle(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.run_angle(100, 100))
        self.assertIsNone(motor.run_angle(100, 100, Stop.COAST))
        self.assertIsNone(motor.run_angle(100, 100, Stop.COAST, False))

    def test_run_target(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.run_target(100, 100))
        self.assertIsNone(motor.run_target(100, 100, Stop.HOLD))
        self.assertIsNone(motor.run_target(100, 100, Stop.HOLD, False))

    def test_run_until_stalled(self):
        motor = Motor(Port.A)

        result = motor.run_until_stalled(100)
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

        result = motor.run_until_stalled(100, Stop.HOLD)
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

        result = motor.run_until_stalled(100, Stop.HOLD, 50)
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_dc(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.dc(100))

    def test_track_target(self):
        motor = Motor(Port.A)
        self.assertIsNone(motor.track_target(100))
