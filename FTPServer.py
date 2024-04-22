#!/usr/bin/python3

import socket
import argparse

SERVER_IP = '127.0.0.1'
SERVER_PORT = 21
DIRECTORY_LOCATION = "./"
username = "cs4440"
password = "cs4440"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--port', type=int, help='Port Number')
    parser.add_argument('--dir', type=str, help='Directory location')
    parser.add_argument('--user', type=str, help='Username')
    parser.add_argument('--password', type=str, help='Password')

    args = parser.parse_args()

    if args.p is not None:
        SERVER_PORT = args.p

    if args.dir is not None:
        DIRECTORY_LOCATION = args.dir

    if args.user is not None:
        username = args.user

    if args.password is not None:
        password = args.password