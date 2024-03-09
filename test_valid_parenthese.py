import unittest
from valid_parentheses import solution

class TestValidParenthases(unittest.TestCase):
    def test_true_result(self):
        self.assertEqual(solution("({{}})"), True)

    def test_false_result(self):
        self.assertEqual(solution("[({)]"), False)

if __name__ == '__main__':
    unittest.main()