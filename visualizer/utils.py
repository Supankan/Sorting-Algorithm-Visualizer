# visualizer/utils.py
import random


def generate_random_array(size, min_value=10, max_value=100):
    """
    Generate a random array of integers of given size and value range.
    :param size: The number of elements in the array.
    :param min_value: Minimum value of an element.
    :param max_value: Maximum value of an element.
    :return: A list containing the random elements.
    """
    return [random.randint(min_value, max_value) for _ in range(size)]
