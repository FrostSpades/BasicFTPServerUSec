#!/usr/bin/python3

from ftplib import FTP
import argparse

FTP_HOST = 'localhost'
FTP_PORT = 21
FTP_USER = 'cs4440'
FTP_PASSWORD = 'cs4440'


def ftp_client():
    try:
        # Begin connection
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        # Perform server command

        # Log out and close connection
        ftp.quit()
    except Exception as error:
        print("Error connecting to server:", str(error))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('-host', type=str, help='Server Host')
    parser.add_argument('-p', type=int, help='Port Number')
    parser.add_argument('-user', type=str, help='Username')
    parser.add_argument('-password', type=str, help='Password')
    parser.add_argument('-file', type=str, help='File')
    parser.add_argument('-command', type=str, help='FTP command')

    args = parser.parse_args()

    if args.host is not None:
        FTP_HOST = args.host

    if args.p is not None:
        FTP_PORT = args.p

    if args.user is not None:
        FTP_USER = args.user

    if args.password is not None:
        FTP_PASSWORD = args.password