from unittest import TestCase
from pybricks.messaging.__stub.__numericmailbox import NumericMailbox
from pybricks.messaging.__stub.__bluetoothmailboxclient import BluetoothMailboxClient


class TestNumericMailbox(TestCase):
    def test_constructor(self):
        try:
            NumericMailbox('name', BluetoothMailboxClient())
        except:
            self.fail()

    def test_read(self):
        box = NumericMailbox('name', BluetoothMailboxClient())
        self.assertIsInstance(box.read(), int)
        self.assertEqual(box.read(), 0)

    def test_send(self):
        box = NumericMailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.send(1.5, 'brick'))
        self.assertIsNone(box.send(15, 'brick'))

    def test_wait(self):
        box = NumericMailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.wait())

    def test_wait_new(self):
        box = NumericMailbox('name', BluetoothMailboxClient())
        self.assertIsInstance(box.wait_new(), int)
        self.assertEqual(box.wait_new(), 0)
