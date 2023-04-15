## This section creates a grpc client-server in vanilla Python. 

### Dependencies:
- grpcio
- grpcio-tools=1.44.0
- mysql-connector-python

(*Note: The grpcio-tools version is fixed to 1.44.0 so as not to break compatibility with mysql-connector-python.*)

To run the code, simply launch `python bookdetails_server.py` in one terminal.
Then in another terminal, launch `python bookdetails_client.py` and type an author's name in the prompt based on the provided list. 
Otherwise, an empty bracket is returned.
