from pybricks.parameters import Port


class TouchSensor:
    """
    LEGO® MINDSTORMS® NXT Touch Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        ...

    def pressed(self) -> bool:
        """
        Checks if the sensor is pressed.

        Returns:
            True if the sensor is pressed, False if it is not pressed.
        """
        return False
