import socket
from threading import Thread, Lock
import sys

class MServer:
    __server_address = ('', 9999)

    def __init__(self, host, port):
        if host != "" and port > 5000:
            self.__server_address = (host, port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "socket connecting to %s port %s\n" % self.__server_address
        self.__sock.bind(self.__server_address)
        self.__sock.listen(5)

    def run(self):
        self.__lock = Lock()
        while True:
            conn, client_add = self.__sock.accept()
            self.__create_conversation(conn, client_add)
    
    def __create_conversation(self, conn, address):
        t = Thread(target=self.__start_conversation, args=(conn, address))
        t.start()

    def __start_conversation(self, conn, address):
        try:
            while True:
                data = conn.recv(1024)
                if data:
                    self.__lock.acquire()
                    print "message from %s: %s\n" % (address, data)
                    r = raw_input("write answer: ")
                    conn.send(r)
                    self.__lock.release()

        finally:
            self.__lock.release()
            conn.close()


s = MServer('172.17.8.107', 9999)
s.run()
