import math
from typing import Optional


def temp_convert(arg: Optional[float]) -> Optional[float]:
    # This function takes either float or None and returns either None or a converted temperature
    # Input: Optional[float]
    # Output: Optional[float]

    # Sample Input: 5
    # Sample Output: 41.0

    # Your Code here:
    try:
        float(arg)
        return True

    except ValueError:
        return False


temp_convert(3.0)