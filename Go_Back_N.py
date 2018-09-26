'''

Author: Sakar Kumar Koot.

Email - sakarkoot@gmail.com


'''
import socket
import threading
import sys
from time import sleep
class Server:

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	fail_ack = []

	def process(self, connect,cli_addr):

		for  i in range(5):
			print("Sending Frame no."+str(i+1))
			connect.send(bytes(str(i+1) ,'utf-8'))
			sleep(0.5)
		print("Waiting for Acknowledgement...")
		for i in range(5):

			j = connect.recv(8).decode('utf-8')
			print("Ack received for frame number :"+str(i+1)+" as :"+str(j))
			j = int(j)
			if (i+1)!= j:
				self.fail_ack.append(i)
		print("Resending Frames...")


		k = min(self.fail_ack)

		for i in range(k,5):
			print("Sending Frame no.")
			connect.send(bytes(str(i+1) ,'utf-8'))
			sleep(0.5)

			print(str(i+1))

	def __init__(self):

		self.server.bind(('0.0.0.0', 10000))
		self.server.listen(1)

		print("Server now Online...")

		connect ,cli_addr = self.server.accept()

		self.process(connect, cli_addr)
		self.server.close()


class Client:

	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	def process(self):

		for i in range(5):
			k = self.sock.recv(8).decode('utf-8')
			print("Received frame no. "+str(k))

		print("Sending Ack..")

		for i in range(5):

			print("Sending Ack fro frame no. "+str(i+1))
			if i!=2:
				self.sock.send(bytes(str(i+1) ,'utf-8'))
				sleep(0.5)
			else:
				self.sock.send(bytes(str(99), 'utf-8'))
				sleep(0.5)
		for i in range(2,5):
			print("Received Frame no. ")
			k = self.sock.recv(8).decode('utf-8')

			print(str(k))
	def __init__(self, server_addr):
		self.sock.connect((server_addr, 10000))
		print("Connected To Server...")

		print("Receiving Frames From Server..")

		self.process()
		self.sock.close()

if(len(sys.argv) >1):
	client = Client(sys.argv[1])

else:
	server=Server()

#####################################
