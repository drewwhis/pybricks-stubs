from pybricks.ev3devices import (Motor)
from pybricks.parameters import (Stop)


class DriveBase:
    """
    Class representing a robotic vehicle with two powered wheels and optional wheel caster(s).
    """

    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: float, axle_track: float):
        """
        Class representing a robotic vehicle with two powered wheels and optional wheel caster(s).

        ----------
        left_motor : Motor – The motor that drives the left wheel.

        right_motor : Motor – The motor that drives the right wheel.

        wheel_diameter : float – Diameter of the wheels (mm).

        axle_track : float – Distance between the midpoints of the two wheels (mm).
        """
        ...

        def drive(self, speed: float, steering: float):
            """
            Start driving at the specified speed and turnrate, 
            both measured at the center point between the wheels ofthe robot.

            ----------
            speed : float – Forward speed of the robot (mm/s).

            steering : float - Turn rate of the robot (deg/s).
            """
            ...

        def drive_time(self, speed: float, steering: float, time: float):
            """
            Drive at the specified speed and turnrate for a given amount of time, and then stop.

            ----------
            speed : float – Forward speed of the robot (mm/s).

            steering : float – Turn rate of the robot (deg/s).

            time : float – Duration of the maneuver (ms).
            """
            ...

        def stop(self, stop_type: Stop = Stop.COAST):
            """
            Stop the robot.

            ----------
            stop_type : Stop – Whether to coast, brake, or hold (Default: Stop.COAST).
            """
            ...
