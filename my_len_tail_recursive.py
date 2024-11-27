"""
Custom implementation of the len() function using tail recursion.

This module provides a function `my_len_tail_recursive` that calculates the length of an iterable
without using the built-in `len()` function. It uses a tail-recursive helper function to count
the elements in the iterable. The code includes detailed documentation and test cases for clarity.

Author: [Your Name]
Date: [Today's Date]
"""

def my_len_tail_recursive(iterable):
    """
    Calculate the length of an iterable using a tail-recursive approach.

    This function determines the number of elements in an iterable by recursively iterating through
    it and incrementing an accumulator. It handles None inputs gracefully by returning 0.

    Parameters:
        iterable (Iterable): The iterable whose length is to be calculated.

    Returns:
        int: The number of elements in the iterable.

    Raises:
        TypeError: If the input is not iterable.

    Examples:
        >>> my_len_tail_recursive([1, 2, 3])
        3
        >>> my_len_tail_recursive("hello")
        5
        >>> my_len_tail_recursive(None)
        0
        >>> my_len_tail_recursive(123)
        Traceback (most recent call last):
            ...
        TypeError: 'int' object is not iterable
    """
    def helper(it, acc):
        """
        Tail-recursive helper function to count elements in the iterator.

        Parameters:
            it (Iterator): An iterator over the iterable.
            acc (int): The accumulator counting the number of elements.

        Returns:
            int: The total count of elements.
        """
        try:
            next(it)
            return helper(it, acc + 1)
        except StopIteration:
            return acc

    if iterable is None:
        return 0
    try:
        iterator = iter(iterable)
    except TypeError:
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    return helper(iterator, 0)

if __name__ == "__main__":
    # Importing unittest for testing
    import unittest

    class TestMyLenTailRecursive(unittest.TestCase):
        """Unit tests for my_len_tail_recursive function."""

        def test_string(self):
            self.assertEqual(my_len_tail_recursive("hello world!"), 12)

        def test_list(self):
            self.assertEqual(my_len_tail_recursive([1, 2, 3, 4, 5]), 5)

        def test_empty_list(self):
            self.assertEqual(my_len_tail_recursive([]), 0)

        def test_none(self):
            self.assertEqual(my_len_tail_recursive(None), 0)

        def test_generator(self):
            gen = (i for i in range(10))
            self.assertEqual(my_len_tail_recursive(gen), 10)

        def test_exhausted_generator(self):
            gen = (i for i in range(5))
            list(gen)  # Exhaust the generator
            self.assertEqual(my_len_tail_recursive(gen), 0)

        def test_set(self):
            self.assertEqual(my_len_tail_recursive({1, 2, 3, 4, 5}), 5)

        def test_tuple(self):
            self.assertEqual(my_len_tail_recursive((1, 2, 3)), 3)

        def test_dictionary(self):
            self.assertEqual(my_len_tail_recursive({'a': 1, 'b': 2, 'c': 3}), 3)

        def test_custom_iterator(self):
            class CountUpTo:
                """Custom iterator that counts up to a maximum number."""
                def __init__(self, max):
                    self.current = 0
                    self.max = max
                def __iter__(self):
                    return self
                def __next__(self):
                    if self.current < self.max:
                        self.current += 1
                        return self.current
                    else:
                        raise StopIteration()

            counter = CountUpTo(5)
            self.assertEqual(my_len_tail_recursive(counter), 5)

        def test_non_iterable(self):
            with self.assertRaises(TypeError):
                my_len_tail_recursive(123)

        def test_bytes(self):
            self.assertEqual(my_len_tail_recursive(b'byte string'), 11)

        def test_bytearray(self):
            self.assertEqual(my_len_tail_recursive(bytearray(b'byte array')), 10)

    # Run the tests
    unittest.main()
