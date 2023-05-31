"""
Sacred Spiral Compression

This code implements a compression algorithm based on the concept of a sacred spiral.
The algorithm encodes the input data by arranging it in a spiral pattern and then decoding it back to its original form.

Usage:
1. Define the input data to be compressed.
2. Call the `sacred_spiral_encode` function to compress the data.
3. Call the `sacred_spiral_decode` function to decompress the encoded data.

Example:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encoded_data = sacred_spiral_encode(data)
decoded_data = sacred_spiral_decode(encoded_data, len(data))

Note: This code is a proof of concept and may not be suitable for all types of data compression scenarios.

Author: Sundeepan Sen
"""

import math


def sacred_spiral_encode(data):
    """
    Encode the input data using the sacred spiral compression algorithm.

    Args:
        data: A list of elements to be compressed.

    Returns:
        encoded_data: The compressed data as a list.
    """
    n = len(data)
    num_layers = math.ceil(math.sqrt(n))
    spiral = [[0] * num_layers for _ in range(num_layers)]
    x, y = num_layers // 2, num_layers // 2
    dx, dy = 0, -1

    for i in range(n):
        spiral[x][y] = data[i]
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    encoded_data = []
    for row in spiral:
        encoded_data.extend(row)

    return encoded_data[:n]


def sacred_spiral_decode(encoded_data, original_length):
    """
    Decode the encoded data using the sacred spiral compression algorithm.

    Args:
        encoded_data: The compressed data as a list.
        original_length: The length of the original uncompressed data.

    Returns:
        decoded_data: The decompressed data as a list.
    """
    n = original_length
    num_layers = math.ceil(math.sqrt(n))
    spiral = [[0] * num_layers for _ in range(num_layers)]
    x, y = num_layers // 2, num_layers // 2
    dx, dy = 0, -1

    for i in range(n):
        spiral[x][y] = encoded_data[i]
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    decoded_data = []
    for i in range(num_layers):
        decoded_data.extend(spiral[i][:num_layers])

    return decoded_data[:n]


# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original Data:", data)

encoded_data = sacred_spiral_encode(data)
print("Encoded Data:", encoded_data)

decoded_data = sacred_spiral_decode(encoded_data, len(data))
print("Decoded Data:", decoded_data)
