import unittest
from count_tokens import count_tokens

class TestCountTokens(unittest.TestCase):

    def test_count_is_correct(self):
        num_tokens = count_tokens("tiktoken is great!")
        self.assertEqual(num_tokens, 6)

if __name__ == '__main__':
    unittest.main()