# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from base import BaseGraph
from copy import deepcopy

class DAGraph(BaseGraph):

	class ValidationError(Exception): pass

	def independent(self):

		all_nodes, dependent = set(self._nodes.itervalues()), set()
		for node in self._nodes.itervalues():
			for dep in node.list_connections(): dependent.add(dep)

		return list(all_nodes - dependent)

	def connect(self, src, dest):

		assert (src in self and dest in self)

		mock = deepcopy(self._nodes)
		mock[src].add_connection(dest)

		if self._validate_structure(mock):
			self._nodes[src].add_connection(dest)
	def disconnect(self, src, dest):

		assert (src in self and dest in self)
		self._nodes[src].remove_connection(dest)
	def change_connection(self, src, original, dest):

		self.disconnect(src, original)
		self.connect(src, dest)
	def add_connections(self, connections):

		for connection in connections:

			src, dest = connection
			self.connect(src, dest)

	def _validate_structure(self, mock_map):

		ind = DAGraph._independent(mock_map)
		if len(ind) == 0: raise DAGraph.ValidationError('Graph has no independent nodes')

		to_visit = list(ind)
		nodes = set()

		while bool(to_visit) is True:

			n = to_visit.pop(0)
			nodes.add(n)
			deps = n.list_connections()

			for dep in deps:

				n.remove_connection(dep.id)
				if len([ 1 for node in mock_map.itervalues() if n.id in node ]) == 0:
					to_visit.append(dep)

		if len(nodes) != len(mock_map): raise DAGraph.ValidationError('Graph has circular dependencies')
		return True

	def __str__(self): return 'DAGraph([%s])' % ', '.join(map(str, self._nodes.itervalues()))
	def __repr__(self): return 'DAGraph(nodes: [%s])' % ', '.join(map(repr, self._nodes.itervalues()))

	@staticmethod
	def _independent(mock_map):

		all_nodes, dependent = set(mock_map.itervalues()), set()
		for node in mock_map.itervalues():
			for dep in node.list_connections(): dependent.add(dep)

		return list(all_nodes - dependent)
