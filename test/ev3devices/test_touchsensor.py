from unittest import TestCase
from pybricks.ev3devices.__stub.__touchsensor import TouchSensor
from pybricks.parameters.__stub.__port import Port


class TestTouchSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, TouchSensor, Port.A)
        self.assertRaises(ValueError, TouchSensor, Port.B)
        self.assertRaises(ValueError, TouchSensor, Port.C)
        self.assertRaises(ValueError, TouchSensor, Port.D)

        try:
            TouchSensor(Port.S1)
            TouchSensor(Port.S2)
            TouchSensor(Port.S3)
            TouchSensor(Port.S4)
        except:
            self.fail()

    def test_pressed(self):
        sensor = TouchSensor(Port.S1)
        value = sensor.pressed()
        self.assertIsInstance(value, bool)
        self.assertFalse(value)