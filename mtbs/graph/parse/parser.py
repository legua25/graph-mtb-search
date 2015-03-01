# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .visitor import GraphVisitor
else:
    from visitor import GraphVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\rI\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write(u"\b\t\b\4\t\t\t\3\2\3\2\5\2\25\n\2\3\3\3\3\5\3\31\n\3")
        buf.write(u"\3\4\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\5\4$\n\4")
        buf.write(u"\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6/\n\6\3\7\6\7")
        buf.write(u"\62\n\7\r\7\16\7\63\3\b\3\b\5\b8\n\b\3\b\3\b\3\b\3\b")
        buf.write(u"\7\b>\n\b\f\b\16\bA\13\b\5\bC\n\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\2\2\n\2\4\6\b\n\f\16\20\2\2J\2\22\3\2\2\2\4\26\3\2\2")
        buf.write(u"\2\6\32\3\2\2\2\b\'\3\2\2\2\n.\3\2\2\2\f\61\3\2\2\2\16")
        buf.write(u"\65\3\2\2\2\20F\3\2\2\2\22\24\5\4\3\2\23\25\5\f\7\2\24")
        buf.write(u"\23\3\2\2\2\24\25\3\2\2\2\25\3\3\2\2\2\26\30\5\20\t\2")
        buf.write(u"\27\31\5\6\4\2\30\27\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2")
        buf.write(u"\2\32#\7\3\2\2\33 \5\b\5\2\34\35\7\4\2\2\35\37\5\b\5")
        buf.write(u"\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!")
        buf.write(u"$\3\2\2\2\" \3\2\2\2#\33\3\2\2\2#$\3\2\2\2$%\3\2\2\2")
        buf.write(u"%&\7\5\2\2&\7\3\2\2\2\'(\5\20\t\2()\7\6\2\2)*\5\n\6\2")
        buf.write(u"*\t\3\2\2\2+/\7\t\2\2,/\7\b\2\2-/\5\6\4\2.+\3\2\2\2.")
        buf.write(u",\3\2\2\2.-\3\2\2\2/\13\3\2\2\2\60\62\5\16\b\2\61\60")
        buf.write(u"\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64")
        buf.write(u"\r\3\2\2\2\65\67\5\20\t\2\668\5\6\4\2\67\66\3\2\2\2\67")
        buf.write(u"8\3\2\2\28B\3\2\2\29:\7\6\2\2:?\5\20\t\2;<\7\4\2\2<>")
        buf.write(u"\5\20\t\2=;\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@C\3")
        buf.write(u"\2\2\2A?\3\2\2\2B9\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\7\7")
        buf.write(u"\2\2E\17\3\2\2\2FG\7\r\2\2G\21\3\2\2\2\13\24\30 #.\63")
        buf.write(u"\67?B")
        return buf.getvalue()


class GraphParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"','", u"'}'", u"':'", u"';'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"Number", u"String", 
                      u"Comment", u"Whitespace", u"Newline", u"ID" ]

    RULE_graph = 0
    RULE_graph_meta_properties = 1
    RULE_meta_properties = 2
    RULE_meta_property = 3
    RULE_meta_value = 4
    RULE_graph_nodes = 5
    RULE_graph_node = 6
    RULE_identifier = 7

    ruleNames =  [ u"graph", u"graph_meta_properties", u"meta_properties", 
                   u"meta_property", u"meta_value", u"graph_nodes", u"graph_node", 
                   u"identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    Number=6
    String=7
    Comment=8
    Whitespace=9
    Newline=10
    ID=11

    def __init__(self, input):
        super(GraphParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GraphContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.GraphContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graph_meta_properties(self):
            return self.getTypedRuleContext(GraphParser.GraphMetaPropertiesContext,0)


        def graph_nodes(self):
            return self.getTypedRuleContext(GraphParser.GraphNodesContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_graph

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_graph(self)
            else:
                return visitor.visitChildren(self)




    def graph(self):

        localctx = GraphParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_graph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.graph_meta_properties()
            self.state = 18
            _la = self._input.LA(1)
            if _la==GraphParser.ID:
                self.state = 17
                self.graph_nodes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphMetaPropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.GraphMetaPropertiesContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext
            self.props = None # Meta_propertiesContext

        def identifier(self):
            return self.getTypedRuleContext(GraphParser.IdentifierContext,0)


        def meta_properties(self):
            return self.getTypedRuleContext(GraphParser.MetaPropertiesContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_graph_meta_properties

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_graph_meta_properties(self)
            else:
                return visitor.visitChildren(self)




    def graph_meta_properties(self):

        localctx = GraphParser.GraphMetaPropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_graph_meta_properties)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            localctx.name = self.identifier()
            self.state = 22
            _la = self._input.LA(1)
            if _la==GraphParser.T__0:
                self.state = 21
                localctx.props = self.meta_properties()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaPropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.MetaPropertiesContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._meta_property = None # Meta_propertyContext
            self.props = list() # of Meta_propertyContexts

        def meta_property(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.MetaPropertyContext)
            else:
                return self.getTypedRuleContext(GraphParser.MetaPropertyContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_meta_properties

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_meta_properties(self)
            else:
                return visitor.visitChildren(self)




    def meta_properties(self):

        localctx = GraphParser.MetaPropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_meta_properties)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(GraphParser.T__0)
            self.state = 33
            _la = self._input.LA(1)
            if _la==GraphParser.ID:
                self.state = 25
                localctx._meta_property = self.meta_property()
                localctx.props.append(localctx._meta_property)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GraphParser.T__1:
                    self.state = 26
                    self.match(GraphParser.T__1)
                    self.state = 27
                    localctx._meta_property = self.meta_property()
                    localctx.props.append(localctx._meta_property)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 35
            self.match(GraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaPropertyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.MetaPropertyContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # IdentifierContext
            self.value = None # Meta_valueContext

        def identifier(self):
            return self.getTypedRuleContext(GraphParser.IdentifierContext,0)


        def meta_value(self):
            return self.getTypedRuleContext(GraphParser.MetaValueContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_meta_property

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_meta_property(self)
            else:
                return visitor.visitChildren(self)




    def meta_property(self):

        localctx = GraphParser.MetaPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_meta_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.key = self.identifier()
            self.state = 38
            self.match(GraphParser.T__3)
            self.state = 39
            localctx.value = self.meta_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.MetaValueContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.string = None # Token
            self.number = None # Token
            self.meta = None # Meta_propertiesContext

        def String(self):
            return self.getToken(GraphParser.String, 0)

        def Number(self):
            return self.getToken(GraphParser.Number, 0)

        def meta_properties(self):
            return self.getTypedRuleContext(GraphParser.MetaPropertiesContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_meta_value

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_meta_value(self)
            else:
                return visitor.visitChildren(self)




    def meta_value(self):

        localctx = GraphParser.MetaValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_meta_value)
        try:
            self.state = 44
            token = self._input.LA(1)
            if token in [GraphParser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                localctx.string = self.match(GraphParser.String)

            elif token in [GraphParser.Number]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                localctx.number = self.match(GraphParser.Number)

            elif token in [GraphParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                localctx.meta = self.meta_properties()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphNodesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.GraphNodesContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._graph_node = None # Graph_nodeContext
            self.nodes = list() # of Graph_nodeContexts

        def graph_node(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.GraphNodeContext)
            else:
                return self.getTypedRuleContext(GraphParser.GraphNodeContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_graph_nodes

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_graph_nodes(self)
            else:
                return visitor.visitChildren(self)




    def graph_nodes(self):

        localctx = GraphParser.GraphNodesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_graph_nodes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                localctx._graph_node = self.graph_node()
                localctx.nodes.append(localctx._graph_node)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GraphParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphNodeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.GraphNodeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext
            self.props = None # Meta_propertiesContext
            self._identifier = None # IdentifierContext
            self.neighbors = list() # of IdentifierContexts

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(GraphParser.IdentifierContext,i)


        def meta_properties(self):
            return self.getTypedRuleContext(GraphParser.MetaPropertiesContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_graph_node

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_graph_node(self)
            else:
                return visitor.visitChildren(self)




    def graph_node(self):

        localctx = GraphParser.GraphNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_graph_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            localctx.name = self.identifier()
            self.state = 53
            _la = self._input.LA(1)
            if _la==GraphParser.T__0:
                self.state = 52
                localctx.props = self.meta_properties()


            self.state = 64
            _la = self._input.LA(1)
            if _la==GraphParser.T__3:
                self.state = 55
                self.match(GraphParser.T__3)
                self.state = 56
                localctx._identifier = self.identifier()
                localctx.neighbors.append(localctx._identifier)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GraphParser.T__1:
                    self.state = 57
                    self.match(GraphParser.T__1)
                    self.state = 58
                    localctx._identifier = self.identifier()
                    localctx.neighbors.append(localctx._identifier)
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 66
            self.match(GraphParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(GraphParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def ID(self):
            return self.getToken(GraphParser.ID, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_identifier

        def accept(self, visitor):
            if isinstance( visitor, GraphVisitor ):
                return visitor.visit_identifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = GraphParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            localctx.name = self.match(GraphParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




