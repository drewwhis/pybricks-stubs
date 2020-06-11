from unittest import TestCase
from pybricks.messaging.__stub.__logicmailbox import LogicMailbox
from pybricks.messaging.__stub.__bluetoothmailboxclient import BluetoothMailboxClient


class TestLogicMailbox(TestCase):
    def test_constructor(self):
        try:
            LogicMailbox('name', BluetoothMailboxClient())
        except:
            self.fail()

    def test_read(self):
        box = LogicMailbox('name', BluetoothMailboxClient())
        self.assertIsInstance(box.read(), bool)
        self.assertFalse(box.read())

    def test_send(self):
        box = LogicMailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.send(False, 'brick'))

    def test_wait(self):
        box = LogicMailbox('name', BluetoothMailboxClient())
        self.assertIsNone(box.wait())

    def test_wait_new(self):
        box = LogicMailbox('name', BluetoothMailboxClient())
        self.assertIsInstance(box.wait_new(), bool)
        self.assertFalse(box.wait_new())
