from unittest import TestCase
from pybricks.iodevices.__stub.__i2cdevice import I2CDevice
from pybricks.parameters.__stub.__port import Port


class TestI2CDevice(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, I2CDevice, Port.A, 0)
        self.assertRaises(ValueError, I2CDevice, Port.B, 0)
        self.assertRaises(ValueError, I2CDevice, Port.C, 0)
        self.assertRaises(ValueError, I2CDevice, Port.D, 0)

        try:
            I2CDevice(Port.S1, 0)
            I2CDevice(Port.S2, 0)
            I2CDevice(Port.S3, 0)
            I2CDevice(Port.S4, 0)
        except:
            self.fail()

    def test_read(self):
        sensor = I2CDevice(Port.S1, 0)
        result = sensor.read(0, 0)
        self.assertIsInstance(result, bytes)
        self.assertEqual(bytes.fromhex('00'), result)

    def test_write(self):
        sensor = I2CDevice(Port.S1, 0)
        self.assertIsNone(sensor.write(5))
        self.assertIsNone(sensor.write(5, bytes.fromhex('00')))
