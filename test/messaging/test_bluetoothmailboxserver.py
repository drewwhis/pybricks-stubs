from unittest import TestCase
from pybricks.messaging.__stub.__bluetoothmailboxserver import BluetoothMailboxServer


class TestBluetoothMailboxServer(TestCase):
    def test_wait_for_connection(self):
        server = BluetoothMailboxServer()
        self.assertIsNone(server.wait_for_connection())
        self.assertIsNone(server.wait_for_connection(2))

    def test_close(self):
        server = BluetoothMailboxServer()
        self.assertIsNone(server.close())
