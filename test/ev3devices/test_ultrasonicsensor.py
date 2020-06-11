from unittest import TestCase
from pybricks.ev3devices.__stub.__ultrasonicsensor import UltrasonicSensor
from pybricks.parameters.__stub.__port import Port


class TestUltrasonicSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, UltrasonicSensor, Port.A)
        self.assertRaises(ValueError, UltrasonicSensor, Port.B)
        self.assertRaises(ValueError, UltrasonicSensor, Port.C)
        self.assertRaises(ValueError, UltrasonicSensor, Port.D)

        try:
            UltrasonicSensor(Port.S1)
            UltrasonicSensor(Port.S2)
            UltrasonicSensor(Port.S3)
            UltrasonicSensor(Port.S4)
        except:
            self.fail()

    def test_distance(self):
        sensor = UltrasonicSensor(Port.S1)
        value = sensor.distance()
        self.assertIsInstance(value, int)
        self.assertEqual(0, value)

        value = sensor.distance(True)
        self.assertIsInstance(value, int)
        self.assertEqual(0, value)

    def test_presence(self):
        sensor = UltrasonicSensor(Port.S1)
        value = sensor.presence()
        self.assertIsInstance(value, bool)
        self.assertFalse(value)
