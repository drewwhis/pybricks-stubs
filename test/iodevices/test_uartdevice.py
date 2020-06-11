from unittest import TestCase
from pybricks.iodevices.__stub.__uartdevice import UARTDevice
from pybricks.parameters.__stub.__port import Port


class TestUARTDevice(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, UARTDevice, Port.A, 0, 0)
        self.assertRaises(ValueError, UARTDevice, Port.B, 0, 0)
        self.assertRaises(ValueError, UARTDevice, Port.C, 0, 0)
        self.assertRaises(ValueError, UARTDevice, Port.D, 0, 0)
        
        try:
            UARTDevice(Port.S1, 0, 0)
            UARTDevice(Port.S2, 0, 0)
            UARTDevice(Port.S3, 0, 0)
            UARTDevice(Port.S4, 0, 0)
        except:
            self.fail()

    def test_read(self):
        sensor = UARTDevice(Port.S1, 0, 0)
        result = sensor.read()
        self.assertIsInstance(result, bytes)
        self.assertEqual(bytes.fromhex('00'), result)

        result = sensor.read(10)
        self.assertIsInstance(result, bytes)
        self.assertEqual(bytes.fromhex('00'), result)

    def test_read_all(self):
        sensor = UARTDevice(Port.S1, 0, 0)
        result = sensor.read_all()
        self.assertIsInstance(result, bytes)
        self.assertEqual(bytes.fromhex('00'), result)

    def test_write(self):
        sensor = UARTDevice(Port.S1, 0, 0)
        self.assertIsNone(sensor.write(bytes.fromhex('00')))

    def test_waiting(self):
        sensor = UARTDevice(Port.S1, 0, 0)
        result = sensor.waiting()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_clear(self):
        sensor = UARTDevice(Port.S1, 0, 0)
        self.assertIsNone(sensor.clear())
    