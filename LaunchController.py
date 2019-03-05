import socket
import sys
from fnv import fnv1a_32

PORT = 8274

if __name__ == "__main__":
	server_address = ('', PORT)

	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
		sock.bind(server_address)
		print('Starting up on port {}...'.format(server_address[1]))

		while True:
			data, address = sock.recvfrom(4096)

			print('Received {} bytes from {}: {}'.format(len(data), address, data))

			if not data:
				continue

			in_hash = int.from_bytes(data[-4:], byteorder='big')
			in_data = data[:-4]
			print(in_data)
			print(hex(in_hash))
			print(hex(fnv1a_32(in_data)))

			reply = ''

			if in_hash != fnv1a_32(in_data):
				reply = b'MISMATCH'
				print("FNV mismatch!")
			else:
				reply = in_data
				print("Good.")

			sent = sock.sendto(reply, address)
			print('Replied {} bytes back.'.format(sent))
