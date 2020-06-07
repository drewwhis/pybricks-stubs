from pybricks.parameters import Port


class TemperatureSensor:
    """
    LEGO® MINDSTORMS® NXT Temperature Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        ...

    def temperature(self) -> int:
        """
        Measures the temperature.

        Returns:
            Measured temperature in degrees Celsius.
        """
        return 0
