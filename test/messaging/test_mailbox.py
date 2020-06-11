from unittest import TestCase
from pybricks.messaging.__stub.__mailbox import Mailbox
from pybricks.messaging.__stub.__bluetoothmailboxclient import BluetoothMailboxClient


class TestMailbox(TestCase):
    def test_constructor(self):
        try:
            Mailbox('name', BluetoothMailboxClient())
            Mailbox('name', BluetoothMailboxClient(), lambda: True)
            Mailbox('name', BluetoothMailboxClient(),
                    lambda: True, lambda: False)
        except:
            self.fail()

    def test_read(self):
        box = Mailbox('name', BluetoothMailboxClient())
        self.assertIsNotNone(box.read())

    def test_send(self):
        box = Mailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.send('test', 'brick'))

    def test_wait(self):
        box = Mailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.wait())

    def test_wait_new(self):
        box = Mailbox('name', BluetoothMailboxClient())
        self.assertIsNotNone(box.wait_new())
