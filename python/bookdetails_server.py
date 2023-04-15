from concurrent import futures
import logging
import grpc
import bookdetails_pb2
import bookdetails_pb2_grpc
import os
import mysql.connector

config = {
    'user': os.getenv('DBUSER'),
    'password': os.getenv('DBPASS'),
    'host': os.getenv('DBHOST'),
    'database': os.getenv('DBSQLENDPOINTS'),
    'raise_on_warnings': True
}

class BookDetails(bookdetails_pb2_grpc.BookDetailsServicer):
    def GetBookDetails(self, request, context):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = ("select name as book_author, title as book_title, quote as book_quote from authors "
                 "inner join titles on authors.id=author_id "
                 "inner join quotes on titles.id=title_id "
                 "where name='%s'" % request.author)
        cursor.execute(query)
        book_data = []
        for (book_author, book_title, book_quote) in cursor:
            book_data.append(bookdetails_pb2.BookDetailsData(
                author=book_author, title=book_title, quotes=book_quote))

        cursor.close()
        cnx.close()

        return bookdetails_pb2.BookDetailsResponse(bookDetails=book_data)

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bookdetails_pb2_grpc.add_BookDetailsServicer_to_server(BookDetails(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
