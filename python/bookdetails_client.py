from __future__ import print_function
import logging
import grpc
import bookdetails_pb2
import bookdetails_pb2_grpc

class BookDetailsDisplay():
    def get_input(self, text):
        return input(text)

    def run(self):
        author_name = self.get_input("Enter author's name: ")
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = bookdetails_pb2_grpc.BookDetailsStub(channel)
            response = stub.GetBookDetails(bookdetails_pb2.BookDetailsRequest(author=author_name.strip()))

        pretty_booklist = []
        for rbd in response.bookDetails:
            pretty_booklist.append([rbd.author, rbd.title, rbd.quotes])

        print(pretty_booklist)

if __name__ == '__main__':
    logging.basicConfig()
    BookDetailsDisplay().run()
