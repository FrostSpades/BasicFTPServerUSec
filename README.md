# Basic FTP Server and Client
This is a basic FTP server and client implementation used for creating packet data in Wireshark.

Made for the University of Utah CS 4440 security class.

# Installation
The release contains two folders. A server folder and a client folder. Each folder holds its associated python file.
The server and client are separated into different folders to show the behavior of file transfer between the two.
For example, downloading a file from the server will take the file that is in the server folder and download it into
the client server.
## Windows Installation
Download the zip file with the following link:

[https://github.com/FrostSpades/BasicFTPServerUSec/releases/download/v1.0/FTPServerClientv1.0.zip](https://github.com/FrostSpades/BasicFTPServerUSec/releases/download/v1.0/FTPServerClientv1.0.zip)

Or alternatively, download the zip from this github's release.
The zip file contains all the associated files described.

## Linux Installation
Download the zip file with the following command:
```
wget https://github.com/FrostSpades/BasicFTPServerUSec/releases/download/v1.0/FTPServerClientv1.0.zip
```
Unzip the file with the following command:
```
unzip FTPServerClientv1.0
```

# How to Use

## Installing pyftpdlib
This code requires pyftpdblib to be installed. This can be done from an IDE environment. Alternatively,
use the following command to install:
```
pip3 install pyftpdlib
```

## Quickstart Guide
The server runs and listens to connections continuously. To quickly use the server, run the server with:
```
python3 FTPServer.py
```
The client runs a quick command and then exits. To download a file from the server, run the following command (parameters are explained later). NOTE: The server needs the file in its directory in order to be downloaded. This can be done by placing a file into the same directory as the FTPServer.py file.
```
python3 FTPClient.py --file filename --retr
```
To upload a file to the server, run the following command:
```
python3 FTPClient.py --file filename --stor
```
# Parameters Guide
## Client Parameters
- `--host hostname`
  - hostname specifies the host name the FTP client should connect to
- `--port portnum`
  - portnum specifies the port number of the server the FTP client intends to connec to
- `--user username`
  - username specifies the username to log in to the FTP server
- `--password password`
  - password specifies the password to log in to the FTP server
- `--file filename`
  - filename specifies the file name of the file used in the request
- `--retr`
  - specifies that the FTP client intends to submit a RETR request
- `--stor`
  - specifies that the FTP client intends to submit a STOR request
## Server Parameters
- `--host hostname`
  - hostname specifies the host name the FTP client should bind to
- `--port portnum`
  - portnum specifies the port number the FTP client should bind to
- `--dir directory`
  - directory specifies the directory that contains the server's files
- `--user username`
  - username specifies the username required to log into the server
- `--password password`
  - password specifies the password required to log into the server
# Using Wireshark
Because this isn't traditional network interaction, wireshark will need to be configured to listen to loopback traffic.
Luckily, this is very simple.

1. Open Wireshark.

2. After opening, in the middle of the screen, you can specify the capture. Double click the "Adapter for loopback traffic capture".

![image](https://github.com/FrostSpades/BasicFTPServerUSec/assets/22160160/4308cf30-e336-43ce-8c7f-c76cc26fd536)

3. It will automatically start collecting data. Now, you should run the client/server request.
   
4. Finally, stop the capture using the red square in the top left and save the pcap file.
