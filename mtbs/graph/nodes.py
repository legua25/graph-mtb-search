# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Node(object):

	def __init__(self, id, meta):

		self._id = id
		self.meta = meta
		self.children = {}

	@property
	def id(self): return self._id
	@property
	def cost(self): return self.meta['cost'] if 'cost' in self.meta else 1

	def connects_to(self, id): return id == self.id or id in self.children
	def list_connections(self, heuristic, goal):

		def __cmp__(n1, n2):

			v1, v2 = n1.cost + heuristic(n1, goal), n2.cost + heuristic(n2, goal)
			return cmp(v1, v2)

		connections = [ node for node in self.children.itervalues() ]
		connections.sort(cmp = __cmp__)

		return connections

	def __str__(self): return '%s' % self.id
	def __repr__(self): return '%s(meta: %s, children: [ %s ])' % (self.id, self.meta, ', '.join([ str(n) for n in self.children ]))
