#! /usr/bin/python
# vim: ts=4 noexpandtab
#
# Battlefield II -- default remote console client
#
# This is a very simple, TCP based remote console client which does MD5 digest
# password authentication.
#
# Recognized command-line options are -h for host and -p for port.
#
# Copyright (c)2004 Digital Illusions CE AB
# Author: Andreas `dep' Fredriksson

import md5
import socket
import errno

# Concats a seed string with the password and returns an ASCII-hex MD5 digest.
def digest(seed, pw):
	if not pw: return None
	m = md5.new()
	m.update(seed)
	m.update(pw)
	return m.hexdigest()

# Client class.
class RconClient:
	def __init__(self):
		self.sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		self.trace = 0
		self.challenge = None

	def connect (self, host, port):
		self.sock.connect ((host, port))
		response = self.getWelcomeResponse()

		# Dig out the seed
		prefix = '### Digest seed: '
		challpos = response.find(prefix)
		if challpos != -1:
			challpos += len(prefix)
			challend = response.find('\n', challpos)
			self.challenge = response[challpos:challend]
			if self.trace: print "S: challenge: ", self.challenge
		if self.trace: print "S:", response
		return response

	def invoke (self, cmd):
		if self.trace: print "C:", cmd
		self.sock.send ('\x02' + cmd + '\n') # This is a non-interactive command.
		response = self.getResponse()
		if self.trace: print "S:", response
		return response

	# Read data until two newlines are encountered
	def getWelcomeResponse (self):
		result = ""
		while 1:
			data = self.sock.recv(1024)
			result += data
			lflfpos = result.find('\n\n')
			if lflfpos != -1: break
		return result

	def getResponse (self):
		result = ""
		done = False
		while not done:
			data = self.sock.recv(1024)
			for c in data:
				if c == '\x04':
					done = True
					break
				result += c
		return result



if __name__ == '__main__':
	from getopt import getopt
	import sys

	host = 'localhost'
	port = 4711

	opts, args = getopt(sys.argv[1:], 'h:p:')
	for k, v in opts:
		if k == '-h': host = v
		elif k == '-p': port = int(v)

	print 'Connecting to %s, port %d..' % (host, port)

	try:
		conn = RconClient()
		conn.connect(host, port)
		while 1:
			pw = raw_input('Password: ')
			d = digest(conn.challenge, pw)
			result = conn.invoke('login %s' % d)
			if result.startswith('Authentication success'): break
			print 'Invalid password, please try again'

		while 1:
			cmd = raw_input('rcon> ')
			if cmd == 'login':
				print 'Already authenticated'
				continue

			if cmd == 'quit': break
			result = conn.invoke(cmd)
			print result

	except socket.error, detail:
		print 'Network error:', detail[1]

	except EOFError:
		pass
