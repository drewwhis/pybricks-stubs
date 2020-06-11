from unittest import TestCase
from pybricks.nxtdevices.__stub.__vernieradapter import VernierAdapter
from pybricks.parameters.__stub.__port import Port


class TestVernierAdapter(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, VernierAdapter, Port.A)
        self.assertRaises(ValueError, VernierAdapter, Port.B)
        self.assertRaises(ValueError, VernierAdapter, Port.C)
        self.assertRaises(ValueError, VernierAdapter, Port.D)
        self.assertRaises(ValueError, VernierAdapter, Port.A, lambda:True)
        self.assertRaises(ValueError, VernierAdapter, Port.B, lambda:True)
        self.assertRaises(ValueError, VernierAdapter, Port.C, lambda:True)
        self.assertRaises(ValueError, VernierAdapter, Port.D, lambda:True)

        try:
            VernierAdapter(Port.S1)
            VernierAdapter(Port.S2)
            VernierAdapter(Port.S3)
            VernierAdapter(Port.S4)
            VernierAdapter(Port.S1, lambda:False)
            VernierAdapter(Port.S2, lambda:False)
            VernierAdapter(Port.S3, lambda:False)
            VernierAdapter(Port.S4, lambda:False)
        except:
            self.fail()

    def test_voltage(self):
        sensor = VernierAdapter(Port.S1)
        result = sensor.voltage()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_conversion(self):
        sensor = VernierAdapter(Port.S1)
        result = sensor.conversion(0)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_value(self):
        sensor = VernierAdapter(Port.S1)
        result = sensor.value()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)
