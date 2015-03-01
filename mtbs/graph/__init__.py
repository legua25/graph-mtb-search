# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from parse import Lexer, Parser, Visitor, FileStream, CommonTokenStream, ParseTreeWalker
from nodes import Node

class Graph(object):

	def __init__(self, meta, nodes):

		self.id = meta.pop('id')
		self.meta = meta
		self.nodes = { i: Node(n['id'], n['meta']) for i, n in nodes.iteritems() }

		for i, value in nodes.iteritems():

			connections = value['connections']
			self.nodes[i].children = { c: self.nodes[c] for c in connections }

	def __getitem__(self, id): return self.nodes[id]

	def __str__(self): return 'Graph(%s, nodes: [ %s ])' % (self.id, ', '.join([ str(node) for node in self.nodes ]))
	def __repr__(self): return 'Graph(id: %id, meta: %s, nodes: [ %s ])' % (self.id, self.meta, ', '.join([ node.id for node in self.nodes ]))

class GraphFactory(Visitor):

	def visit_graph(self, ctx):

		# Get meta properties for graph file
		meta_properties = self.visit_graph_meta_properties(ctx.graph_meta_properties())

		# Get nodes composing graph; return an empty list if none
		if ctx.graph_nodes() is not None: nodes = self.visit_graph_nodes(ctx.graph_nodes())
		else: nodes = []

		return {
			'meta': meta_properties,
		    'nodes': nodes
		}

	# This block parses the graph header and meta-properties
	def visit_graph_meta_properties(self, ctx):

		# Get meta properties header as a single map
		meta = { 'id': self.visit_identifier(ctx.name) }
		if ctx.props is not None: meta.update(self.visit_meta_properties(ctx.props))

		return meta
	def visit_meta_properties(self, ctx):

		meta = {}
		# Iterate through every mapping, returning the stored values from there
		for prop in ctx.props:

			key, value = self.visit_meta_property(prop)
			meta[key] = value

		return meta
	def visit_meta_property(self, ctx):

		# Return a key-value pair for each meta entry; nested meta properties are already taken care of
		return self.visit_identifier(ctx.key), self.visit_meta_value(ctx.value)
	def visit_meta_value(self, ctx):

		# Parse the value to its adequate representation, use the "meta_property" rule for nested properties
		if ctx.string is not None: value = ctx.string.text[1:-1]
		elif ctx.number is not None: value = float(ctx.number.text)
		else: value = self.visit_meta_properties(ctx.meta)

		return value
	def visit_identifier(self, ctx): return ctx.name.text

	# This block parses each graph node and returns them as a list of dicts
	def visit_graph_nodes(self, ctx):

		nodes = {}
		for i, node in enumerate(ctx.nodes):

			value = self.visit_graph_node(node)
			id = value['id']

			if id in nodes:

				token = node.start
				raise Exception('Node ID "%s" is being redefined (line: %i, col: %i)' % (id, token.line, token.column))

			nodes[id] = value

		return nodes
	def visit_graph_node(self, ctx):

		# Pack the information within a dict for later analysis and usage
		return {
			'id': self.visit_identifier(ctx.name),
			'meta': {} if ctx.props is None else self.visit_meta_properties(ctx.props),
			'connections': [ self.visit_identifier(id) for id in ctx.neighbors ]
		}

	@staticmethod
	def from_file(path):

		# Define source parsing utilities
		source = FileStream(path)
		lexer = Lexer(source)
		tokens = CommonTokenStream(lexer)
		parser, walker = Parser(tokens), ParseTreeWalker()

		# Parse the file and generate intermediate output
		data = GraphFactory().visit_graph(parser.graph())
		return Graph(data['meta'], data['nodes'])
