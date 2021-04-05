#!/usr/bin/env python3


import socket
import argparse


HOST = '192.168.1.10'  # The server's hostname or IP address
PORT = 5000            # The port used by the server

COMMANDS = {
    'set':  0x01,
    'get':  0x10,
    'buzz': 0x02,
    'led':  0x03,
    'auto': 0x81,
}

HEADER = bytes([
    0xAA,
    0xBB,
    0x03,
])
 
FOOTER = bytes([0xEE])


def sendCmd(cmd, val=0, retlen=0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(HEADER + bytes([COMMANDS[cmd], val]) + FOOTER)
        return s.recv(retlen)


def getPort():
    data = sendCmd('get', retlen=6)
    return int(data[4]) + 1


def setPort(port):
    data = sendCmd('set', port, retlen=6)
    return int(data[4]) + 1


def mute():
    data = sendCmd('buzz', 0x0)


def unmute():
    data = sendCmd('buzz', 0x01)


def autoscan():
    data = sendCmd('auto', 0x01)


def noautoscan():
    data = sendCmd('auto', 0x0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Interact with the TESmart KVM switch over TCP/IP.')
    parser.add_argument('command', help='specify the command; one of: get, set, mute, unmute, autoscan, noautoscan')
    parser.add_argument('-p', '--port', type=int,
                        help='an integer for specifying the KVM port')
    args = parser.parse_args()

    if args.command == 'get':
        print(f"Current port: {getPort()}")
    elif args.command == 'set':
        print(f"Current port: {getPort()}")
        print(f"New port: {setPort(args.port)}")
    elif args.command == 'mute':
        mute()
        print("Muted.")
    elif args.command == 'unmute':
        unmute()
        print("Unmuted.")
    elif args.command == 'autoscan':
        autoscan()
        print("Auto scanning.")
    elif args.command == 'noautoscan':
        noautoscan()
        print("Disabling auto scan.")
    else:
        print("Nothing to do.")
