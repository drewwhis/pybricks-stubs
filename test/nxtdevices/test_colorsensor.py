from unittest import TestCase
from pybricks.nxtdevices.__stub.__colorsensor import ColorSensor
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
        self.assertEqual(result, Color.BLACK)

    def test_ambient(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.ambient()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_reflection(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.reflection()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_rgb(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.rgb()
        self.assertIsInstance(result, tuple)
        self.assertEqual(3, len(result))
        self.assertIsInstance(result[0], int)
        self.assertEqual(0, result[0])
        self.assertIsInstance(result[1], int)
        self.assertEqual(0, result[1])
        self.assertIsInstance(result[2], int)
        self.assertEqual(0, result[2])

    def test_light_on(self):
        sensor = ColorSensor(Port.S1)
        self.assertIsNone(sensor.light.on(Color.RED))

    def test_light_off(self):
        sensor = ColorSensor(Port.S1)
        self.assertIsNone(sensor.light.off())
