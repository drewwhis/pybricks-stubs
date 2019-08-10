def print(*value, sep: str = ' ', end: str = '\n', file, flush):
    """
    Print values on the terminal or a stream

    ----------
    value - List of things to print (according to Python print()).

    sep : str - The string that separates the arguments in value (Default: space).

    end : str = The string that ends the print (Default: new line).
    """
    ...


def wait(time: float):
    """
    Pause the user program for a specified amount of time.

    ----------
    time : float - How long to wait in milliseconds
    """
    ...


class StopWatch:
    """
    A stopwatch to measure time intervals. 
    Similar to the stopwatch feature on your phone.
    """

    def time(self) -> float:
        """
        Get the current time of the stopwatch.

        ----------
        Returns - Elapsed time.
        Return type - time: ms
        """
        ...

    def pause(self):
        """
        Pause the stopwatch.
        """
        ...

    def resume(self):
        """
        Resume the stopwatch.
        """
        ...

    def reset(self):
        """
        Reset the stopwatch time to 0.
        The run state is unaffected:
        - If it was paused, it stays paused (but now at 0).
        - If it was running, it stays running (but starting again from 0)
        """
        ...
