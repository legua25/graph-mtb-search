# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class GraphNode(object):

	def __init__(self, id, graph, **params):

		self._id = id
		self._connections = {}
		self._graph = graph

		for param, value in params.iteritems():
			setattr(self, param, value)

	@property
	def id(self): return self._id

	def add_connection(self, id, cost = 0.0):

		assert (id in self._graph)
		self._connections[id] = cost
	def remove_connection(self, id):

		if id in self:
			del self._connections[id]
	def list_connections(self):

		def __get__(id): return self._graph[id]
		return list(map(__get__, self._connections))
	def is_connected_to(self, id): return id == self.id or id in self
	def estimate_cost_to(self, id):

		if id not in self: return float('inf')
		return self._connections[id]
	def to_template_string(self): return '%s: %s;' % (self._id, ', '.join(map(str, self.list_connections())))

	def __contains__(self, item): return item in self._connections
	def __eq__(self, other): return isinstance(other, GraphNode) and self.id == other.id
	def __ne__(self, other): return self.__eq__(other) is False
	def __str__(self): return self.id
	def __repr__(self): return 'GraphNode(id: %s)' % self.id

class BaseGraph(object):

	class DuplicateNode(Exception): pass
	class InvalidNode(Exception): pass

	node_class = GraphNode

	def __init__(self):
		self._nodes = {}

	def add_node(self, id, **params):

		assert isinstance(id, str)

		if id in self._nodes: raise BaseGraph.DuplicateNode('Node "%s" already exists in this graph' % id)
		self._nodes[id] = self.node_class(id, self, **params)
	def remove_node(self, id):

		if id not in self._nodes: raise BaseGraph.InvalidNode('Node "%s" does not exist in this graph' % id)

		del self._nodes[id]
		for node in self._nodes.itervalues():
			node.remove_connection(id)
	def add_nodes(self, *nodes):

		for node in nodes:

			try: id, params = node
			except ValueError: id, params = node, {}

			self.add_node(id, **params)
	def remove_nodes(self, *nodes):
		for id in nodes: self.remove_node(id)
	def clear(self): self._nodes = {}

	def connect(self, src, dest): raise NotImplementedError()
	def disconnect(self, src, dest): raise NotImplementedError()
	def change_connection(self, src, original, dest): raise NotImplementedError()
	def add_connections(self, connections): raise NotImplementedError()
	def list_connections(self, id, exclude = lambda n: True):
		return list(filter(exclude, [ node_id for node_id, node in self._nodes.iteritems() if id in node ]))

	def __contains__(self, id): return id in self._nodes
	def __getitem__(self, id):

		if id not in self: raise BaseGraph.InvalidNode('Node "%s" does not exist in this graph' % id)
		return self._nodes[id]
	def __delitem__(self, id): self.remove_node(id)
	def __iter__(self):
		for id in self._nodes: yield self._nodes[id]
	def __str__(self): return 'BaseGraph([%s])' % ', '.join(map(str, self._nodes.itervalues()))
	def __repr__(self): return 'BaseGraph(nodes: [%s])' % ', '.join(map(repr, self._nodes.itervalues()))
class Graph(BaseGraph):

	def connect(self, src, dest, cost = 0.0, bidir = True):

		assert (src in self and dest in self)

		n = self._nodes[src]
		n.add_connection(dest, cost = cost)

		if bidir:

			n = self._nodes[dest]
			n.add_connection(src, cost = cost)
	def disconnect(self, src, dest):

		assert (src in self and dest in self)

		n = self._nodes[src]
		n.remove_connection(dest)

		n = self._nodes[dest]
		n.remove_connection(src)
	def change_connection(self, src, original, dest, bidir = True):

		self.disconnect(src, original)
		self.connect(src, dest, bidir = bidir)
	def add_connections(self, connections, bidir = True):

		for connection in connections:

			try: src, dest, cost = connection
			except ValueError:

				src, dest = connection
				cost = 0.0
			self.connect(src, dest, cost = cost, bidir = bidir)

	def __str__(self): return 'Graph([%s])' % ', '.join(map(str, self._nodes.itervalues()))
	def __repr__(self): return 'Graph(nodes: [%s])' % ', '.join(map(repr, self._nodes.itervalues()))
