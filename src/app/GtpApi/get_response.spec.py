from get_response import get_gtp_response, gtp_trim
import unittest

class TestGetResponse(unittest.TestCase):

    def test_trim_works(self):
        old_text = "gptrim is really quite great! Is it not?"
        new_text = gtp_trim(old_text)
        self.assertEqual(len(new_text) < len(old_text), True)

if __name__ == '__main__':
    unittest.main()