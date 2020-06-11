from unittest import TestCase
from pybricks.iodevices.__stub.__analogsensor import AnalogSensor
from pybricks.parameters.__stub.__port import Port


class TestAnalogSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, AnalogSensor, Port.A)
        self.assertRaises(ValueError, AnalogSensor, Port.B)
        self.assertRaises(ValueError, AnalogSensor, Port.C)
        self.assertRaises(ValueError, AnalogSensor, Port.D)

        try:
            AnalogSensor(Port.S1)
            AnalogSensor(Port.S2)
            AnalogSensor(Port.S3)
            AnalogSensor(Port.S4)
        except:
            self.fail()

    def test_voltage(self):
        sensor = AnalogSensor(Port.S1)
        result = sensor.voltage()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_resistance(self):
        sensor = AnalogSensor(Port.S1)
        result = sensor.resistance()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_active(self):
        sensor = AnalogSensor(Port.S1)
        self.assertIsNone(sensor.active())

    def test_passive(self):
        sensor = AnalogSensor(Port.S1)
        self.assertIsNone(sensor.passive())
