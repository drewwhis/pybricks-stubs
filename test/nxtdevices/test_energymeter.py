from unittest import TestCase
from pybricks.nxtdevices.__stub.__energymeter import EnergyMeter
from pybricks.parameters.__stub.__port import Port


class TestEnergyMeter(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, EnergyMeter, Port.A)
        self.assertRaises(ValueError, EnergyMeter, Port.B)
        self.assertRaises(ValueError, EnergyMeter, Port.C)
        self.assertRaises(ValueError, EnergyMeter, Port.D)

        try:
            EnergyMeter(Port.S1)
            EnergyMeter(Port.S2)
            EnergyMeter(Port.S3)
            EnergyMeter(Port.S4)
        except:
            self.fail()

    def test_storage(self):
        sensor = EnergyMeter(Port.S1)
        result = sensor.storage()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_input(self):
        sensor = EnergyMeter(Port.S1)
        result = sensor.input()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], int)
        self.assertEqual(result[0], 0)
        self.assertIsInstance(result[1], int)
        self.assertEqual(result[1], 0)
        self.assertIsInstance(result[2], int)
        self.assertEqual(result[2], 0)

    def test_output(self):
        sensor = EnergyMeter(Port.S1)
        result = sensor.output()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], int)
        self.assertEqual(result[0], 0)
        self.assertIsInstance(result[1], int)
        self.assertEqual(result[1], 0)
        self.assertIsInstance(result[2], int)
        self.assertEqual(result[2], 0)
