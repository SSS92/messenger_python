import socket
from threading import Thread

class MClient:
	def __init__(self, host, port):
                self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__sock.connect((host, port))
	def run(self):
		while True:
			self.__send_message()
			self.__recive_message()

	def __send_message(self):
		message = raw_input("insert message : ")
		self.__sock.send(message)

	def __recive_message(self):
		message = self.__sock.recv(1024)
		print "message from server : %s" % message

c = MClient('172.17.8.107',9999)
c.run()

