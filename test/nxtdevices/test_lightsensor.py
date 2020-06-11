from unittest import TestCase
from pybricks.nxtdevices.__stub.__lightsensor import LightSensor
from pybricks.parameters.__stub.__port import Port


class TestLightSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, LightSensor, Port.A)
        self.assertRaises(ValueError, LightSensor, Port.B)
        self.assertRaises(ValueError, LightSensor, Port.C)
        self.assertRaises(ValueError, LightSensor, Port.D)

        try:
            LightSensor(Port.S1)
            LightSensor(Port.S2)
            LightSensor(Port.S3)
            LightSensor(Port.S4)
        except:
            self.fail()

    def test_ambient(self):
        sensor = LightSensor(Port.S1)
        result = sensor.ambient()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_reflection(self):
        sensor = LightSensor(Port.S1)
        result = sensor.reflection()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)
