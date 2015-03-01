# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from graph.nodes import Node

class Navigator(object):

	def __init__(self, graph):
		self.graph = graph

	def run(self, start, goal, **kwargs):

		start = self.graph[start]
		goal = self.graph[goal]

		return self.navigate_to(start, goal, **kwargs)
	def navigate_to(self, start, goal, **kwargs): pass

class Path(object):

	def __init__(self, node, parent = None, **meta):

		self._parent = parent
		self._node = node
		self.meta = meta

		self.list_connections = node.list_connections
		self.connects_to = node.connects_to

	@property
	def id(self): return self._node.id
	@property
	def node(self): return self._node
	@property
	def parent(self): return self._parent

	def __str__(self): return '(%s -> %s)' % ('<start>' if self.parent is None else self.parent, self.id)
	def __repr__(self): return 'Path(parent: %s, node: %i, meta: %s)' % ('<start>' if self.parent is None else self.parent, self.id, self.meta)

class NowherePath(Path):

	def __init__(self):

		n = Node('<nowhere>', {})
		Path.__init__(self, n, parent = n)

	def __str__(self): return 'Path(<nowhere>)'
	def __repr__(self): return 'Path(<nowhere>)'
NOWHERE = NowherePath()
