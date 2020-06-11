from unittest import TestCase
from pybricks.ev3devices.__stub.__gyrosensor import GyroSensor
from pybricks.parameters.__stub.__port import Port
from pybricks.parameters.__stub.__direction import Direction


class TestGyroSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, GyroSensor, Port.A)
        self.assertRaises(ValueError, GyroSensor, Port.B)
        self.assertRaises(ValueError, GyroSensor, Port.C)
        self.assertRaises(ValueError, GyroSensor, Port.D)
        
        try:
            GyroSensor(Port.S1)
            GyroSensor(Port.S2)
            GyroSensor(Port.S3)
            GyroSensor(Port.S4)
        except:
            self.fail()

        try:
            GyroSensor(Port.S1, Direction.CLOCKWISE)
            GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
        except:
            self.fail()

    def test_speed(self):
        sensor = GyroSensor(Port.S1)
        value = sensor.speed()
        self.assertIsInstance(value, int)
        self.assertEqual(0, value)

    def test_angle(self):
        sensor = GyroSensor(Port.S1)
        value = sensor.angle()
        self.assertIsInstance(value, int)
        self.assertEqual(0, value)

    def test_reset_angle(self):
        sensor = GyroSensor(Port.S1)
        self.assertIsNone(sensor.reset_angle(100))
