from unittest import TestCase
from pybricks.ev3devices.__stub.__colorsensor import ColorSensor
from pybricks.parameters.__stub.__port import Port
from pybricks.parameters.__stub.__color import Color


class TestColorSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, ColorSensor, Port.A)
        self.assertRaises(ValueError, ColorSensor, Port.B)
        self.assertRaises(ValueError, ColorSensor, Port.C)
        self.assertRaises(ValueError, ColorSensor, Port.D)

        try:
            ColorSensor(Port.S1)
            ColorSensor(Port.S2)
            ColorSensor(Port.S3)
            ColorSensor(Port.S4)
        except:
            self.fail()

    def test_color(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.color()
        self.assertIsInstance(result, Color)
        self.assertEqual(Color.BLACK, result)

    def test_ambient(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.ambient()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_reflection(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.reflection()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_rgb(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.rgb()
        self.assertIsInstance(result, tuple)
        self.assertEqual(3, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])
        self.assertEqual(0, result[2])
