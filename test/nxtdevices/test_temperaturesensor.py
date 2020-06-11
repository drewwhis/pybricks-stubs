from unittest import TestCase
from pybricks.nxtdevices.__stub.__temperaturesensor import TemperatureSensor
from pybricks.parameters.__stub.__port import Port


class TestTemperatureSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, TemperatureSensor, Port.A)
        self.assertRaises(ValueError, TemperatureSensor, Port.B)
        self.assertRaises(ValueError, TemperatureSensor, Port.C)
        self.assertRaises(ValueError, TemperatureSensor, Port.D)

        try:
            TemperatureSensor(Port.S1)
            TemperatureSensor(Port.S2)
            TemperatureSensor(Port.S3)
            TemperatureSensor(Port.S4)
        except:
            self.fail()

    def test_temperature(self):
        sensor = TemperatureSensor(Port.S1)
        result = sensor.temperature()
        self.assertIsInstance(result, float)
        self.assertEqual(0.0, result)
