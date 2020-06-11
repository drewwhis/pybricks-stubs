from unittest import TestCase
from pybricks.messaging.__stub.__bluetoothmailboxclient import BluetoothMailboxClient


class TestBluetoothMailboxClient(TestCase):
    def test_connect(self):
        client = BluetoothMailboxClient()
        self.assertIsNone(client.connect('brick'))

    def test_close(self):
        client = BluetoothMailboxClient()
        self.assertIsNone(client.close())