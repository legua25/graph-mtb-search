# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from src.graph.base import BaseGraph, GraphNode

class Path(object):

	def __init__(self, node, parent = None, cost = 0.0):

		assert isinstance(node, GraphNode)

		self._node = node
		self._parent = parent
		self._cost = cost

		self.list_connections = node.list_connections
		self.is_connected_to = node.is_connected_to
		self.estimate_cost_to = node.estimate_cost_to

		if parent is not None: assert isinstance(parent, Path)

	@property
	def node(self): return self._node
	@property
	def parent(self): return self._parent
	@property
	def id(self): return self._node.id
	@property
	def cost(self): return self._cost

	def __iter__(self):

		node = self
		while node is not None:

			yield node
			node = node.parent
	def __str__(self):

		if self._parent is not None: return self.id
		else: return '(%s > %s)' % (self._parent.id, self.id)
	def __repr__(self): return 'Path(id: %s, parent: %s, cost: %.8f)' % (self.id, self._parent, self._cost)

NOWHERE = Path(GraphNode('<nowhere>', None))

class Navigator(object):

	path_class = Path

	def __init__(self, graph):

		assert isinstance(graph, BaseGraph)
		self.graph = graph

	def navigate(self, start, end, **kwargs):

		initial, goal = self.graph[start], self.graph[end]
		return self.navigate_to(initial, goal, **kwargs)
	def navigate_to(self, start, end, **kwargs): raise NotImplementedError()
