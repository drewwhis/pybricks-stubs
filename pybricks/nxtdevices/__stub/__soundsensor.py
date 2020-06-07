from pybricks.parameters import Port


class SoundSensor:
    """
    LEGO® MINDSTORMS® NXT Sound Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        ...

    def intensity(self, audible_only: bool = True) -> int:
        """
        Measures the ambient sound intensity (loudness).

        Args:
            audible_only (bool): Detect only audible sounds. This tries to filter out frequencies that cannot be heard by the human ear.

        Returns:
            Sound intensity as a percentage (0 to 100).
        """
        return 0
