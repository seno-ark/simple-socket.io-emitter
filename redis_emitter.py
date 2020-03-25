# -*- coding: utf-8 -*-
#!/usr/bin/env python


import redis
import msgpack


class Emitter:
	EVENT_TYPE = 2

	def __init__(self, host, port):

		self.uid = ''
		self._room = None
		self._nsp = None

		# create redis client
		self._client = redis.StrictRedis(host=host, port=port)


	def room(self, room):
		"""
		Set Room
		"""
		self._room = room
		return self


	def nsp(self, nsp):
		"""
		Set Namespace
		"""
		self._nsp = nsp
		return self


	def emit(self, *args):
		"""
		Emit

		args:
		- event_name
		- payload
		"""

		if not self._nsp:
			self._nsp = "/"
		if not self._room:
			self._room = ""

		packet = {
			'data': args,
			'type': self.EVENT_TYPE
		}

		channel = "#".join(("socket.io", self._nsp, self._room, ""))

		self._client.publish(channel, msgpack.packb([self.uid, packet]))
