import unittest
from bookdetails_server import BookDetails
import bookdetails_pb2

class TestBookDetailsServer(unittest.TestCase):
    def test_grpc_server(self):
        service = BookDetails()
        bdresponse = service.GetBookDetails(bookdetails_pb2.BookDetailsRequest(author='Kurt Vonnegut'), None)
        bd_arr = []
        for bdr in bdresponse.bookDetails:
            bd_arr.append([bdr.author, bdr.title, bdr.quotes])
        vonnegut_row = ['Kurt Vonnegut', 'Slaughterhouse-Five', '“So it goes.”']
        self.assertIn(vonnegut_row, bd_arr)

if __name__ == '__main__':
    unittest.main()
