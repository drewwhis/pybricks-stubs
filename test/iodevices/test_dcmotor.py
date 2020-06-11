from unittest import TestCase
from pybricks.iodevices.__stub.__dcmotor import DCMotor
from pybricks.parameters.__stub.__port import Port
from pybricks.parameters.__stub.__direction import Direction


class TestDCMotor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, DCMotor, Port.S1)
        self.assertRaises(ValueError, DCMotor, Port.S2)
        self.assertRaises(ValueError, DCMotor, Port.S3)
        self.assertRaises(ValueError, DCMotor, Port.S4)
        
        try:
            DCMotor(Port.A)
            DCMotor(Port.B)
            DCMotor(Port.C)
            DCMotor(Port.D)
        except:
            self.fail()

        try:
            DCMotor(Port.A, Direction.COUNTERCLOCKWISE)
        except:
            self.fail()

    def test_dc(self):
        motor = DCMotor(Port.A)
        self.assertIsNone(motor.dc(100))

    def test_stop(self):
        motor = DCMotor(Port.A)
        self.assertIsNone(motor.stop())