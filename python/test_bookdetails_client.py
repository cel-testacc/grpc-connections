import unittest
from unittest.mock import patch
from bookdetails_client import BookDetailsDisplay

class TestBookDetailsClient(unittest.TestCase):
    def test_grpc_client(self):
        with (
            patch('bookdetails_client.BookDetailsDisplay.get_input', return_value='Emily St. John Mandel'),
            patch('builtins.print') as mock_print
        ):
            BookDetailsDisplay().run()
            mandel_row = [['Emily St. John Mandel', 'Station Eleven', '“Hell is the absence of the people you long for.”'], ['Emily St. John Mandel', 'Sea of Tranquility', '“My point is, there’s always something. I think, as a species, we have a desire to believe that we’re living at the climax of the story. It’s a kind of narcissism. We want to believe that we’re uniquely important, that we’re living at the end of history, that now, after all these millennia of false alarms, now is finally the worst that it’s ever been, that finally we have reached the end of the world.”']]

            mock_print.assert_called_with(mandel_row)

if __name__ == '__main__':
    unittest.main()
