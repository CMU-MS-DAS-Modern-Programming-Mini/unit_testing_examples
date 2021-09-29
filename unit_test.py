import unittest

class T:
    def __init__(self):
        self.x = 1.000


def add_x_and_k(x, k):
    if isinstance(x, str):
        return x + str(k)
    elif isinstance(x, int):
        return x + int(k)
    elif isinstance(x, float):
        return x + float(k)
    else:
        return "this would be an error"


class TestAddXAndK(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_x_and_k("x", "0.001"), "x0.001")
        self.assertEqual(add_x_and_k(1, 1.022), 2)
        self.assertAlmostEqual(add_x_and_k(1.01, 2.01), 3.02)
        self.assertEqual(add_x_and_k(True, 0.01), "this would be an error")
        y = T()
        self.assertEqual(add_x_and_k(y, 0.001), "this would be an error")


if __name__ == "__main__":
    unittest.main()

    """
    ### Unit testing for module

    pass_flag = True
    if add_x_and_k("x", "0.001") != "x0.001":
        print("string failed")
        pass_flag = False
    if add_x_and_k(1, 1.022) != 2:
        print("int failed")
        pass_flag = False
    if add_x_and_k(1.01, 2.01) != 1.01 + 2.01:
        print("float failed")
        pass_flag = False
    if add_x_and_k(True, 1.020) != "this would be an error":
        print("error failed")
        pass_flag = False

    if pass_flag:
        print("All Tests Passed")
    else:
        print("Some Tests Failed")
    """
