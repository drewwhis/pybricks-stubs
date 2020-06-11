from unittest import TestCase
from pybricks.ev3devices.__stub.__infraredsensor import InfraredSensor
from pybricks.parameters.__stub.__port import Port


class TestInfraredSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, InfraredSensor, Port.A)
        self.assertRaises(ValueError, InfraredSensor, Port.B)
        self.assertRaises(ValueError, InfraredSensor, Port.C)
        self.assertRaises(ValueError, InfraredSensor, Port.D)

        try:
            InfraredSensor(Port.S1)
            InfraredSensor(Port.S2)
            InfraredSensor(Port.S3)
            InfraredSensor(Port.S4)
        except:
            self.fail()

    def test_distance(self):
        sensor = InfraredSensor(Port.S1)
        result = sensor.distance()
        self.assertIsInstance(result, int)
        self.assertEqual(0, result)

    def test_beacon(self):
        sensor = InfraredSensor(Port.S1)
        self.assertRaises(ValueError, sensor.beacon, 0)
        self.assertRaises(ValueError, sensor.beacon, 5)

        result = sensor.beacon(1)
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

        result = sensor.beacon(2)
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

        result = sensor.beacon(3)
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

        result = sensor.beacon(4)
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

    def test_buttons(self):
        sensor = InfraredSensor(Port.S1)
        self.assertRaises(ValueError, sensor.buttons, 0)
        self.assertRaises(ValueError, sensor.buttons, 5)

        result = sensor.buttons(1)
        self.assertIsInstance(result, list)
        result = sensor.buttons(2)
        self.assertIsInstance(result, list)
        result = sensor.buttons(3)
        self.assertIsInstance(result, list)
        result = sensor.buttons(4)
        self.assertIsInstance(result, list)

    def test_keypad(self):
        sensor = InfraredSensor(Port.S1)
        result = sensor.keypad()
        self.assertIsInstance(result, list)
