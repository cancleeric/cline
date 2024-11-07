import unittest
import numpy as np
import sys
sys.path.append('/Users/apple/Desktop/Cline')
from logic_functions import (
    step_function, sigmoid_function, relu_function, weighted_sum,
    identity_function, softmax_function, mean_squared_error, cross_entropy_error,
    numerical_derivative
)

class TestLogicFunctions(unittest.TestCase):
    def test_step_function(self):
        x = np.array([-1.0, 1.0, 2.0])
        expected = np.array([0, 1, 1])
        np.testing.assert_array_equal(step_function(x), expected)

    def test_sigmoid_function(self):
        x = np.array([0.0])
        expected = np.array([0.5])
        np.testing.assert_array_almost_equal(sigmoid_function(x), expected)

    def test_relu_function(self):
        x = np.array([-1.0, 0.0, 1.0])
        expected = np.array([0.0, 0.0, 1.0])
        np.testing.assert_array_equal(relu_function(x), expected)

    def test_weighted_sum(self):
        x = np.array([1.0, 2.0])
        weights = np.array([0.5, 0.5])
        bias = 0.1
        expected = 1.6
        self.assertAlmostEqual(weighted_sum(x, weights, bias), expected)

    def test_identity_function(self):
        x = np.array([1.0, 2.0, 3.0])
        np.testing.assert_array_equal(identity_function(x), x)

    def test_mean_squared_error(self):
        y_true = np.array([1.0, 2.0, 3.0])
        y_pred = np.array([1.0, 2.0, 4.0])
        expected = 0.3333333333333333
        self.assertAlmostEqual(mean_squared_error(y_true, y_pred), expected)

    # Test function
    def test_cross_entropy_error(self):
        y_true = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        y_pred = np.array([[0.8, 0.1, 0.1], [0.1, 0.8, 0.1], [0.1, 0.2, 0.7]])
        expected = 0.2676  # Updated expected value based on manual calculation
        self.assertAlmostEqual(cross_entropy_error(y_true, y_pred), expected, places=3)

    def test_numerical_derivative(self):
        f = lambda x: x**2
        x = 3.0
        expected = 6.0  # f'(x) = 2x, so f'(3) = 6
        self.assertAlmostEqual(numerical_derivative(f, x), expected, places=5)

if __name__ == "__main__":
    unittest.main()