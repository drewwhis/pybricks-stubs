from pybricks.parameters import Port


class LUMPDevice:
    """
    Devices using the LEGO UART Messaging Protocol.

    Args:
        port (Port): Port to which the device is connected.
    """

    def __init__(self, port: Port):
        ...

    def read(self, mode: int) -> tuple:
        """
        Reads values from a given mode.

        Args:
            mode (int): Device mode.s

        Returns:
            Values read from the sensor.
        """
        return ()

    def write(self, mode: int, data: tuple):
        """
        Writes values to the sensor. Only selected sensors and modes support this.

        Args:
            mode (int): Device mode.
            data (tuple): Values to be written.
        """
        ...
