# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by GraphParser.

class GraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphParser#graph.
    def visit_graph(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graph_meta_properties.
    def visit_graph_meta_properties(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#meta_properties.
    def visit_meta_properties(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#meta_property.
    def visit_meta_property(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#meta_value.
    def visit_meta_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graph_nodes.
    def visit_graph_nodes(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graph_node.
    def visit_graph_node(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#identifier.
    def visit_identifier(self, ctx):
        return self.visitChildren(ctx)


