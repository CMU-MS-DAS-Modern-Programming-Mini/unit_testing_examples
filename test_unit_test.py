from unit_test import *


def test_add_x_and_k_string():
    """
    Verifies string output
    """

    assert add_x_and_k("x", "0.001") == "x0.001"


def test_add_x_and_k_int():
    """
    Verifies integer output
    """

    assert add_x_and_k(1,  1.022) == 2


def test_add_x_and_k_float():
    """
    Verifies float output
    """

    assert round(add_x_and_k(1.01, 2.01), 2) == 3.02


def test_add_x_and_k_bool():
    """
    Verifies that this should fail with a boolean
    """

    assert add_x_and_k(True, 0.001) == "this would be an error"


def test_add_x_and_k_error():
    """
    Verifies that this should fail with an error
    """

    t = T()
    assert add_x_and_k(t, 0.001) == "this would be an error"
