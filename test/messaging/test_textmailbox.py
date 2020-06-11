from unittest import TestCase
from pybricks.messaging.__stub.__textmailbox import TextMailbox
from pybricks.messaging.__stub.__bluetoothmailboxclient import BluetoothMailboxClient


class TestTextMailbox(TestCase):
    def test_constructor(self):
        try:
            TextMailbox('name', BluetoothMailboxClient())
        except:
            self.fail()

    def test_read(self):
        box = TextMailbox('name', BluetoothMailboxClient())
        self.assertIsInstance(box.read(), str)
        self.assertEqual(box.read(), "")

    def test_send(self):
        box = TextMailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.send("test", 'brick'))

    def test_wait(self):
        box = TextMailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.wait())

    def test_wait_new(self):
        box = TextMailbox('name', BluetoothMailboxClient())
        self.assertIsInstance(box.wait_new(), str)
        self.assertEqual(box.wait_new(), "")
