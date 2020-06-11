from unittest import TestCase
from pybricks.nxtdevices.__stub.__soundsensor import SoundSensor
from pybricks.parameters.__stub.__port import Port


class TestSoundSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, SoundSensor, Port.A)
        self.assertRaises(ValueError, SoundSensor, Port.B)
        self.assertRaises(ValueError, SoundSensor, Port.C)
        self.assertRaises(ValueError, SoundSensor, Port.D)

        try:
            SoundSensor(Port.S1)
            SoundSensor(Port.S2)
            SoundSensor(Port.S3)
            SoundSensor(Port.S4)
        except:
            self.fail()

    def test_intensity(self):
        sensor = SoundSensor(Port.S1)
        result = sensor.intensity()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

        result = sensor.intensity(False)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)
