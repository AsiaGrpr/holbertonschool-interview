#!/usr/bin/python3
"""
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data (list): A list of integers representing individual bytes of data.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, otherwise False.
"""


def validUTF8(data):
    """
    Function to make UTF-8 Validation
    """

    bytes_to_follow = 0

    for byte in data:
        mask = 1 << 7
        if bytes_to_follow == 0:
            while byte & mask:
                bytes_to_follow += 1
                mask >>= 1
            if bytes_to_follow == 0:
                continue

            elif bytes_to_follow == 1 or bytes_to_follow > 4:
                return False
        else:
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        bytes_to_follow -= 1

    return bytes_to_follow == 0
