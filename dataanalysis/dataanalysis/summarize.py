"""Summarize data values to support data analysis."""

# TODO: incorrect all of the needed type annotations


def compute_mean(numbers: List[float]) -> float:
    """Compute the mean of a list of numbers."""
    # TODO: Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # TODO: sum the list of the numbers
    # TODO: determine the length of the list of numbers
    # TODO: as long as the computation will not be an
    # undefined division by zero, compute the mean
    # https://stackoverflow.com/questions/58400652/average-returning-a-value-even-when-list-is-empty
    # TODO: if the list was empty, then return a mean that is "not a number"
    # https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values


def compute_median(numbers: List[float]) -> float:
    """Compute the median of a list of numbers."""
    # TODO: Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # TODO: as long as the computation will not be an
    # undefined division by zero, compute the median
    # TODO: sort the numbers in an "in place" fashion
        # TODO: case: the count of the values is even
        # TODO: get the two indices that are before and after the middle
        # TODO: convert to an integer to prepare for indexing
        # adjust for the fact that lists index starting at 0
        # TODO: compute the median value
        # TODO: case: the count of the values is odd
        # TODO: convert to an integer to prepare for indexing
        # adjust for the fact that lists index starting at 0
    # TODO: if the list was empty, then return a median that is "not a number"
    # TODO: return the computed median value


def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # TODO: Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # TODO: compute the mean
    # TODO: compute the differences from the mean
    # TODO: return the computed differences from the mean


def compute_variance(numbers: List[float]) -> float:
    """Compute the variance of a list of numbers."""
    # TODO: compute the difference from the mean
    # TODO: compute the squared differences
    # TODO: calculate the variance
    # TODO: return the calculated variance of the list of numbers


def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    # TODO: call the function to calculate the variance
    # TODO: calculate the standard deviation as the square root of the variance
    # TODO: return the calculated standard devision of the list of numbers
