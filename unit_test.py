"""
Example code for unit_testing methods
"""
import unittest


class T:
    """
    Just a class to make something different
    """

    def __init__(self):
        """
        Instance Creation Operator
        """
        self.x = 1.000


def add_x_and_k(x, k):
    """
    Simple function that checks types
    """

    if isinstance(x, str):
        return x + str(k)
    elif isinstance(x, int):
        return x + int(k)
    elif isinstance(x, float):
        return x + float(k)
    else:
        return "this would be an error"


class TestAddXAndK(unittest.TestCase):
    """
    A unitest module test case for the module
    """

    def test_add(self):
        """
        Testing the add function
        """
        self.assertEqual(add_x_and_k("x", "0.001"), "x0.001")
        self.assertEqual(add_x_and_k(1, 1.022), 2)
        self.assertAlmostEqual(add_x_and_k(1.01, 2.01), 3.02)
        self.assertEqual(add_x_and_k(True, 0.01), "this would be an error")
        y = T()
        self.assertEqual(add_x_and_k(y, 0.001), "this would be an error")


if __name__ == "__main__":
    # Unit testing for module
    unittest.main()
