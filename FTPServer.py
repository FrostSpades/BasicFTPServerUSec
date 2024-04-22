#!/usr/bin/python3

import argparse
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

SERVER_IP = '127.0.0.1'
SERVER_PORT = 21
DIRECTORY_LOCATION = "./"
username = "cs4440"
password = "cs4440"


def start_ftp_server():
    # Create an authorizer and add the user
    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, DIRECTORY_LOCATION, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server_address = (SERVER_IP, SERVER_PORT)

    server = FTPServer(server_address, handler)
    server.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--port', type=int, help='Port Number')
    parser.add_argument('--dir', type=str, help='Directory location')
    parser.add_argument('--user', type=str, help='Username')
    parser.add_argument('--password', type=str, help='Password')

    args = parser.parse_args()

    if args.port is not None:
        SERVER_PORT = args.port

    if args.dir is not None:
        DIRECTORY_LOCATION = args.dir

    if args.user is not None:
        username = args.user

    if args.password is not None:
        password = args.password