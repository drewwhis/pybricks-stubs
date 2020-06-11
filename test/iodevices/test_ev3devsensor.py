from unittest import TestCase
from pybricks.iodevices.__stub.__ev3devsensor import Ev3devSensor
from pybricks.parameters.__stub.__port import Port


class TestEv3devSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, Ev3devSensor, Port.A)
        self.assertRaises(ValueError, Ev3devSensor, Port.B)
        self.assertRaises(ValueError, Ev3devSensor, Port.C)
        self.assertRaises(ValueError, Ev3devSensor, Port.D)
        
        try:
            Ev3devSensor(Port.S1)
            Ev3devSensor(Port.S2)
            Ev3devSensor(Port.S3)
            Ev3devSensor(Port.S4)
        except:
            self.fail()

    def test_sensor_index(self):
        sensor = Ev3devSensor(Port.S1)
        result = sensor.sensor_index
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_port_index(self):
        sensor = Ev3devSensor(Port.S1)
        result = sensor.port_index
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_read(self):
        sensor = Ev3devSensor(Port.S1)
        result = sensor.read('mode')
        self.assertIsInstance(result, tuple)
        self.assertEqual(0, len(result))
