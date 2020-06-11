from unittest import TestCase
from pybricks.nxtdevices.__stub.__ultrasonicsensor import UltrasonicSensor
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
        result = sensor.distance()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)
