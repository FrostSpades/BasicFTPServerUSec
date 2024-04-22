#!/usr/bin/python3

from ftplib import FTP
import argparse

FTP_HOST = '127.0.0.2'
FTP_PORT = 21
FTP_USER = 'cs4440'
FTP_PASSWORD = 'cs4440'
FTP_FILE = ""


def ftp_client():
    try:
        # Begin connection
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        # Perform server command
        if args.retr:
            with open(FTP_FILE, 'wb') as file:
                ftp.retrbinary('RETR ' + FTP_FILE, file.write)
            print(f"File '{FTP_FILE} downloaded successfully")

        elif args.stor:
            with open(FTP_FILE, 'rb') as file:
                ftp.storbinary('STOR ' + FTP_FILE, file)
            print(f"File '{FTP_FILE} uploaded successfully")

        # Log out and close connection
        ftp.quit()

    except Exception as error:
        print('\033[91m' + "Error connecting to server: " + str(error) + '\033[0m')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--host', type=str, help='Server Host')
    parser.add_argument('--port', type=int, help='Port Number')
    parser.add_argument('--user', type=str, help='Username')
    parser.add_argument('--password', type=str, help='Password')
    parser.add_argument('--file', type=str, help='File')
    parser.add_argument('--retr', action='store_true', help='RETR command')
    parser.add_argument('--stor', action='store_true', help='STOR command')

    args = parser.parse_args()

    if args.host is not None:
        FTP_HOST = args.host

    if args.port is not None:
        FTP_PORT = args.port

    if args.user is not None:
        FTP_USER = args.user

    if args.password is not None:
        FTP_PASSWORD = args.password

    if args.file is not None:
        FTP_FILE = args.file
    else:
        print('\033[91m' + "Error: Please specify a file using --file" + '\033[0m')
        exit(1)

    if args.retr and args.stor:
        print('\033[91m' + "Error: Both --retr and --stor cannot be enabled at once" + '\033[0m')
        exit(1)

    if not args.retr and not args.stor:
        print('\033[91m' + "Error: Please specify either --retr or --stor" + '\033[0m')
        exit(1)

    ftp_client()