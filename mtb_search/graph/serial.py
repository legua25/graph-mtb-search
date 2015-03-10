# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import choice, randint, uniform
from mtb_search.graph import Graph

def random_str(length, allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
	return str(''.join([ choice(allowed) for _ in range(length) ]))

class GraphBuilder(object):

	@staticmethod
	def create_graph(num_nodes, max_connections, node_name = random_str, name_length = 8, allow_recursive = False, min_connections = 0):

		if num_nodes <= 0: raise ValueError('Number of nodes must be a positive integer greater than 0')
		elif max_connections <= 0: raise ValueError('Number of maximum connections must be a positive integer greater than 0')
		elif max_connections > num_nodes: raise ValueError('Cannot have more connections than number of nodes in graph')
		elif min_connections < 0: raise ValueError('Minimum connections must be a positive integer greater than or equal to 0')
		elif min_connections >= max_connections: raise ValueError('Minimum connections must be less than maximum connections')

		g = Graph()
		nodes = GraphBuilder._create_nodes(g, num_nodes, node_name, name_length)
		GraphBuilder._create_connections(g, nodes, max_connections, min_connections, allow_recursive)

		return g
	@staticmethod
	def _create_nodes(graph, num_nodes, node_name, name_length):

		nodes = []
		for i in range(num_nodes):

			name = node_name(name_length)
			if name in nodes: continue

			nodes.append(name)
			graph.add_node(name)

		return nodes
	@staticmethod
	def _create_connections(graph, nodes, max_connections, min_connections, allow_recursive):

		for i in range(len(nodes)):

			node = nodes[i]
			connections = GraphBuilder._select_connections(node, nodes, max_connections, min_connections, allow_recursive)
			graph.add_connections(connections, bidir = False)
	@staticmethod
	def _select_connections(node, nodes, max_connections, min_connections, allow_recursive):

		num_connect = randint(min_connections, max_connections)
		out = []

		while len(out) < num_connect:

			n = choice(nodes)
			if n not in out:

				if allow_recursive is False and n == node: continue
				elif uniform(0.0, 1.0) >= 0.8: continue

				out.append((node, n))

		return out
