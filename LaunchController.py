import socketserver
import time

class LaunchCommanderListener(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			# self.request is the TCP socket connected to the client
			self.data = b''

			while True:
				incoming = self.request.recv(255)
				self.data += incoming
				if self.data[-1:] == b'\x04':
					print("done.")
					self.data = self.data[:-1]
					break

			print("{} wrote: {}".format(self.client_address[0], self.data))
	#		print("Injecting artifical delay...")
	#		time.sleep(5)

			# just send back the same data, but upper-cased
			self.request.sendall(self.data.upper())
			print("Replied: ", self.data.upper())

if __name__ == "__main__":
	PORT = 8274

	socketserver.TCPServer.allow_reuse_address = True

	server = socketserver.TCPServer(("", PORT), LaunchCommanderListener)
	server.serve_forever()
