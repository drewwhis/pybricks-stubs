from unittest import TestCase
from pybricks.iodevices.__stub.__lumpdevice import LUMPDevice
from pybricks.parameters.__stub.__port import Port


class TestLUMPDevice(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, LUMPDevice, Port.A)
        self.assertRaises(ValueError, LUMPDevice, Port.B)
        self.assertRaises(ValueError, LUMPDevice, Port.C)
        self.assertRaises(ValueError, LUMPDevice, Port.D)
        
        try:
            LUMPDevice(Port.S1)
            LUMPDevice(Port.S2)
            LUMPDevice(Port.S3)
            LUMPDevice(Port.S4)
        except:
            self.fail()

    def test_read(self):
        sensor = LUMPDevice(Port.S1)
        result = sensor.read(0)
        self.assertIsInstance(result, tuple)
        self.assertEqual(0, len(result))

    def test_write(self):
        sensor = LUMPDevice(Port.S1)
        self.assertIsNone(sensor.write(0, ()))
