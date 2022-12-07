import unittest
from main import intervals

class TestCase(unittest.TestCase):

    def test_simple_list(self):
        result = intervals([100, 101])
        self.assertEqual(result, [[100,101]])

    def test_three_numbers(self):
        result = intervals([1, 2, 3])
        self.assertEqual(result, [[1, 3]])

    def test_two_sequences(self):
        result = intervals([1,2,3,5,6])
        self.assertEqual(result, [[1,3], [5,6]])

    def test_three_sequences(self):
        result = intervals([1, 2, 3, 5, 6, 10, 11, 12, 13])
        self.assertEqual(result, [[1,3], [5,6], [10,13]])
    
    def test_many_sequences(self):
        result = intervals([1, 2, 3, 5, 6, 10, 11, 12, 13, 20, 21, 22, 100, 101])
        self.assertEqual(result, [[1,3], [5,6], [10,13], [20,22], [100,101]])
    
    def test_no_sequence(self):
        result = intervals([1,2,5])
        self.assertEqual(result, [[1,2], [5]])

    def test_one_number(self):
        result = intervals([1])
        self.assertEqual(result, [[1]])
    
    def test_nothing_number(self):
        result = intervals([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()