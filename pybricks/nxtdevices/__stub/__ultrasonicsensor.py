from pybricks.parameters import Port


class UltrasonicSensor:
    """
    LEGO® MINDSTORMS® NXT Ultrasonic Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        ...

    def distance(self) -> int:
        """
        Measures the distance between the sensor and an object using ultrasonic sound waves.

        Returns:
            Distance in millimeters.
        """
        return 0
