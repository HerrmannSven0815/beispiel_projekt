import main
import unittest

class TestFibonacci(unittest.TestCase):
    def test_unittest_wrong_types(self):
        with self.assertRaises(TypeError):
            main.fibonacci("test")

    def test_fibonacci(self):
        self.assertEqual(main.fibonacci(1), [1])
        self.assertEqual(main.fibonacci(2), [1, 1])
        self.assertEqual(main.fibonacci(3), [1, 1, 2])
        self.assertEqual(main.fibonacci(4), [1, 1, 2, 3])
        self.assertEqual(main.fibonacci(5), [1, 1, 2, 3, 5])
        self.assertEqual(main.fibonacci(6), [1, 1, 2, 3, 5, 8])
