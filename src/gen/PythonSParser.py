# Generated from /home/Aluno/Downloads/trabalhoFinalCompiladores/PythonS.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,306,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,5,0,50,8,0,10,0,12,0,53,
        9,0,1,0,1,0,1,1,1,1,1,1,3,1,60,8,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,
        3,69,8,3,10,3,12,3,72,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,82,
        8,5,10,5,12,5,85,9,5,1,5,1,5,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,
        1,5,5,5,97,8,5,10,5,12,5,100,9,5,1,5,4,5,103,8,5,11,5,12,5,104,1,
        5,1,5,4,5,109,8,5,11,5,12,5,110,1,6,1,6,1,6,1,6,1,6,1,6,4,6,119,
        8,6,11,6,12,6,120,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,153,8,7,1,8,1,8,1,8,3,8,158,8,8,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,4,
        12,190,8,12,11,12,12,12,191,1,12,1,12,1,12,1,12,4,12,198,8,12,11,
        12,12,12,199,1,12,1,12,3,12,204,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,5,13,214,8,13,10,13,12,13,217,9,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,5,14,226,8,14,10,14,12,14,229,9,14,1,15,1,15,1,
        15,1,15,3,15,235,8,15,1,15,3,15,238,8,15,1,16,1,16,1,16,1,16,1,16,
        3,16,245,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,255,8,
        17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,267,8,
        18,1,19,1,19,1,19,4,19,272,8,19,11,19,12,19,273,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,302,8,19,1,
        20,1,20,1,20,0,2,26,28,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,0,4,1,0,2,6,1,0,41,43,1,0,41,42,2,0,8,8,26,40,
        317,0,45,1,0,0,0,2,56,1,0,0,0,4,63,1,0,0,0,6,65,1,0,0,0,8,73,1,0,
        0,0,10,108,1,0,0,0,12,112,1,0,0,0,14,152,1,0,0,0,16,157,1,0,0,0,
        18,159,1,0,0,0,20,163,1,0,0,0,22,174,1,0,0,0,24,183,1,0,0,0,26,205,
        1,0,0,0,28,218,1,0,0,0,30,237,1,0,0,0,32,239,1,0,0,0,34,254,1,0,
        0,0,36,266,1,0,0,0,38,301,1,0,0,0,40,303,1,0,0,0,42,44,3,2,1,0,43,
        42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,51,1,0,0,
        0,47,45,1,0,0,0,48,50,3,10,5,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,3,12,6,0,
        55,1,1,0,0,0,56,59,3,4,2,0,57,60,3,6,3,0,58,60,3,8,4,0,59,57,1,0,
        0,0,59,58,1,0,0,0,60,61,1,0,0,0,61,62,5,1,0,0,62,3,1,0,0,0,63,64,
        7,0,0,0,64,5,1,0,0,0,65,70,5,41,0,0,66,67,5,7,0,0,67,69,5,41,0,0,
        68,66,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,7,1,0,
        0,0,72,70,1,0,0,0,73,74,5,41,0,0,74,75,5,8,0,0,75,76,7,1,0,0,76,
        9,1,0,0,0,77,78,5,9,0,0,78,79,5,41,0,0,79,83,5,10,0,0,80,82,3,34,
        17,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,
        86,1,0,0,0,85,83,1,0,0,0,86,87,5,11,0,0,87,88,3,4,2,0,88,92,5,12,
        0,0,89,91,3,2,1,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,
        1,0,0,0,93,98,1,0,0,0,94,92,1,0,0,0,95,97,3,10,5,0,96,95,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,102,1,0,0,0,100,98,
        1,0,0,0,101,103,3,14,7,0,102,101,1,0,0,0,103,104,1,0,0,0,104,102,
        1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,13,0,0,107,109,
        1,0,0,0,108,77,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,
        0,0,0,111,11,1,0,0,0,112,113,5,9,0,0,113,114,5,14,0,0,114,115,5,
        10,0,0,115,116,5,11,0,0,116,118,5,12,0,0,117,119,3,14,7,0,118,117,
        1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,122,
        1,0,0,0,122,123,5,13,0,0,123,13,1,0,0,0,124,153,3,20,10,0,125,126,
        3,22,11,0,126,127,5,1,0,0,127,153,1,0,0,0,128,153,3,24,12,0,129,
        130,3,18,9,0,130,131,5,1,0,0,131,153,1,0,0,0,132,153,3,36,18,0,133,
        134,5,41,0,0,134,135,5,41,0,0,135,136,3,40,20,0,136,137,5,41,0,0,
        137,138,5,10,0,0,138,139,3,26,13,0,139,140,5,11,0,0,140,141,5,1,
        0,0,141,153,1,0,0,0,142,143,5,41,0,0,143,144,7,2,0,0,144,153,5,1,
        0,0,145,146,5,41,0,0,146,147,5,10,0,0,147,148,5,41,0,0,148,149,3,
        26,13,0,149,150,5,11,0,0,150,151,5,1,0,0,151,153,1,0,0,0,152,124,
        1,0,0,0,152,125,1,0,0,0,152,128,1,0,0,0,152,129,1,0,0,0,152,132,
        1,0,0,0,152,133,1,0,0,0,152,142,1,0,0,0,152,145,1,0,0,0,153,15,1,
        0,0,0,154,158,3,14,7,0,155,156,5,15,0,0,156,158,5,1,0,0,157,154,
        1,0,0,0,157,155,1,0,0,0,158,17,1,0,0,0,159,160,5,41,0,0,160,161,
        5,8,0,0,161,162,3,26,13,0,162,19,1,0,0,0,163,164,5,16,0,0,164,165,
        5,41,0,0,165,166,5,17,0,0,166,167,5,18,0,0,167,168,5,10,0,0,168,
        169,3,32,16,0,169,170,5,11,0,0,170,171,5,12,0,0,171,172,3,16,8,0,
        172,173,5,13,0,0,173,21,1,0,0,0,174,175,5,19,0,0,175,176,5,12,0,
        0,176,177,3,16,8,0,177,178,5,13,0,0,178,179,5,20,0,0,179,180,5,10,
        0,0,180,181,3,26,13,0,181,182,5,11,0,0,182,23,1,0,0,0,183,184,5,
        21,0,0,184,185,5,10,0,0,185,186,3,26,13,0,186,187,5,11,0,0,187,189,
        5,12,0,0,188,190,3,14,7,0,189,188,1,0,0,0,190,191,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,203,5,13,0,0,194,195,
        5,22,0,0,195,197,5,12,0,0,196,198,3,14,7,0,197,196,1,0,0,0,198,199,
        1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,202,
        5,13,0,0,202,204,1,0,0,0,203,194,1,0,0,0,203,204,1,0,0,0,204,25,
        1,0,0,0,205,206,6,13,-1,0,206,207,3,28,14,0,207,215,1,0,0,0,208,
        209,10,2,0,0,209,210,3,40,20,0,210,211,3,28,14,0,211,212,5,1,0,0,
        212,214,1,0,0,0,213,208,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,
        215,216,1,0,0,0,216,27,1,0,0,0,217,215,1,0,0,0,218,219,6,14,-1,0,
        219,220,3,30,15,0,220,227,1,0,0,0,221,222,10,2,0,0,222,223,3,40,
        20,0,223,224,3,30,15,0,224,226,1,0,0,0,225,221,1,0,0,0,226,229,1,
        0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,29,1,0,0,0,229,227,1,0,
        0,0,230,231,5,10,0,0,231,232,3,26,13,0,232,234,5,11,0,0,233,235,
        5,1,0,0,234,233,1,0,0,0,234,235,1,0,0,0,235,238,1,0,0,0,236,238,
        7,2,0,0,237,230,1,0,0,0,237,236,1,0,0,0,238,31,1,0,0,0,239,240,5,
        42,0,0,240,241,5,23,0,0,241,244,5,42,0,0,242,243,5,23,0,0,243,245,
        5,42,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,33,1,0,0,0,246,247,
        3,4,2,0,247,248,5,41,0,0,248,255,1,0,0,0,249,250,3,4,2,0,250,251,
        5,41,0,0,251,252,5,7,0,0,252,253,3,34,17,0,253,255,1,0,0,0,254,246,
        1,0,0,0,254,249,1,0,0,0,255,35,1,0,0,0,256,257,5,41,0,0,257,258,
        3,40,20,0,258,259,5,24,0,0,259,260,5,10,0,0,260,261,5,11,0,0,261,
        262,5,1,0,0,262,267,1,0,0,0,263,264,3,38,19,0,264,265,5,1,0,0,265,
        267,1,0,0,0,266,256,1,0,0,0,266,263,1,0,0,0,267,37,1,0,0,0,268,269,
        5,25,0,0,269,271,5,10,0,0,270,272,7,2,0,0,271,270,1,0,0,0,272,273,
        1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,302,
        5,11,0,0,276,277,5,25,0,0,277,278,5,10,0,0,278,279,5,43,0,0,279,
        280,5,7,0,0,280,281,7,2,0,0,281,282,3,40,20,0,282,283,7,2,0,0,283,
        284,5,11,0,0,284,302,1,0,0,0,285,286,5,25,0,0,286,287,5,10,0,0,287,
        288,5,43,0,0,288,289,5,7,0,0,289,290,7,2,0,0,290,302,5,11,0,0,291,
        292,5,25,0,0,292,293,5,10,0,0,293,294,5,43,0,0,294,295,5,7,0,0,295,
        296,5,43,0,0,296,302,5,11,0,0,297,298,5,25,0,0,298,299,5,10,0,0,
        299,300,5,43,0,0,300,302,5,11,0,0,301,268,1,0,0,0,301,276,1,0,0,
        0,301,285,1,0,0,0,301,291,1,0,0,0,301,297,1,0,0,0,302,39,1,0,0,0,
        303,304,7,3,0,0,304,41,1,0,0,0,24,45,51,59,70,83,92,98,104,110,120,
        152,157,191,199,203,215,227,234,237,244,254,266,273,301
    ]

class PythonSParser ( Parser ):

    grammarFileName = "PythonS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'real'", "'string'", 
                     "'boolean'", "'void'", "','", "'='", "'def'", "'('", 
                     "')'", "'{'", "'}'", "'main'", "'break'", "'for'", 
                     "'in'", "'range'", "'do'", "'while'", "'if'", "'else'", 
                     "':'", "'input'", "'print'", "'!'", "'-'", "'&&'", 
                     "'||'", "'+'", "'*'", "'/'", "'=='", "'!='", "'>='", 
                     "'<='", "'>'", "'<'", "'+='", "'*='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "STRING", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_decVars = 1
    RULE_type = 2
    RULE_listaIds = 3
    RULE_listaAtribs = 4
    RULE_decFunc = 5
    RULE_blocoMain = 6
    RULE_stmt = 7
    RULE_breakStmt = 8
    RULE_atrib = 9
    RULE_for = 10
    RULE_doWhile = 11
    RULE_if = 12
    RULE_expr = 13
    RULE_term = 14
    RULE_factor = 15
    RULE_range = 16
    RULE_listaParams = 17
    RULE_nativeFunc = 18
    RULE_print = 19
    RULE_operacao = 20

    ruleNames =  [ "prog", "decVars", "type", "listaIds", "listaAtribs", 
                   "decFunc", "blocoMain", "stmt", "breakStmt", "atrib", 
                   "for", "doWhile", "if", "expr", "term", "factor", "range", 
                   "listaParams", "nativeFunc", "print", "operacao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    ID=41
    NUM=42
    STRING=43
    WS=44
    COMMENT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocoMain(self):
            return self.getTypedRuleContext(PythonSParser.BlocoMainContext,0)


        def decVars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.DecVarsContext)
            else:
                return self.getTypedRuleContext(PythonSParser.DecVarsContext,i)


        def decFunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.DecFuncContext)
            else:
                return self.getTypedRuleContext(PythonSParser.DecFuncContext,i)


        def getRuleIndex(self):
            return PythonSParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PythonSParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__1) | (1 << PythonSParser.T__2) | (1 << PythonSParser.T__3) | (1 << PythonSParser.T__4) | (1 << PythonSParser.T__5))) != 0):
                self.state = 42
                self.decVars()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self.decFunc() 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 54
            self.blocoMain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecVarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PythonSParser.TypeContext,0)


        def listaIds(self):
            return self.getTypedRuleContext(PythonSParser.ListaIdsContext,0)


        def listaAtribs(self):
            return self.getTypedRuleContext(PythonSParser.ListaAtribsContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_decVars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecVars" ):
                listener.enterDecVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecVars" ):
                listener.exitDecVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecVars" ):
                return visitor.visitDecVars(self)
            else:
                return visitor.visitChildren(self)




    def decVars(self):

        localctx = PythonSParser.DecVarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decVars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.type_()
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 57
                self.listaIds()
                pass

            elif la_ == 2:
                self.state = 58
                self.listaAtribs()
                pass


            self.state = 61
            self.match(PythonSParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonSParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PythonSParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__1) | (1 << PythonSParser.T__2) | (1 << PythonSParser.T__3) | (1 << PythonSParser.T__4) | (1 << PythonSParser.T__5))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.ID)
            else:
                return self.getToken(PythonSParser.ID, i)

        def getRuleIndex(self):
            return PythonSParser.RULE_listaIds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIds" ):
                listener.enterListaIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIds" ):
                listener.exitListaIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIds" ):
                return visitor.visitListaIds(self)
            else:
                return visitor.visitChildren(self)




    def listaIds(self):

        localctx = PythonSParser.ListaIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listaIds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PythonSParser.ID)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PythonSParser.T__6:
                self.state = 66
                self.match(PythonSParser.T__6)
                self.state = 67
                self.match(PythonSParser.ID)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAtribsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.ID)
            else:
                return self.getToken(PythonSParser.ID, i)

        def NUM(self):
            return self.getToken(PythonSParser.NUM, 0)

        def STRING(self):
            return self.getToken(PythonSParser.STRING, 0)

        def getRuleIndex(self):
            return PythonSParser.RULE_listaAtribs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAtribs" ):
                listener.enterListaAtribs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAtribs" ):
                listener.exitListaAtribs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAtribs" ):
                return visitor.visitListaAtribs(self)
            else:
                return visitor.visitChildren(self)




    def listaAtribs(self):

        localctx = PythonSParser.ListaAtribsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listaAtribs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(PythonSParser.ID)
            self.state = 74
            self.match(PythonSParser.T__7)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.ID) | (1 << PythonSParser.NUM) | (1 << PythonSParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.ID)
            else:
                return self.getToken(PythonSParser.ID, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.TypeContext)
            else:
                return self.getTypedRuleContext(PythonSParser.TypeContext,i)


        def listaParams(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.ListaParamsContext)
            else:
                return self.getTypedRuleContext(PythonSParser.ListaParamsContext,i)


        def decVars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.DecVarsContext)
            else:
                return self.getTypedRuleContext(PythonSParser.DecVarsContext,i)


        def decFunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.DecFuncContext)
            else:
                return self.getTypedRuleContext(PythonSParser.DecFuncContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.StmtContext)
            else:
                return self.getTypedRuleContext(PythonSParser.StmtContext,i)


        def getRuleIndex(self):
            return PythonSParser.RULE_decFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecFunc" ):
                listener.enterDecFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecFunc" ):
                listener.exitDecFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecFunc" ):
                return visitor.visitDecFunc(self)
            else:
                return visitor.visitChildren(self)




    def decFunc(self):

        localctx = PythonSParser.DecFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 77
                    self.match(PythonSParser.T__8)
                    self.state = 78
                    self.match(PythonSParser.ID)
                    self.state = 79
                    self.match(PythonSParser.T__9)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__1) | (1 << PythonSParser.T__2) | (1 << PythonSParser.T__3) | (1 << PythonSParser.T__4) | (1 << PythonSParser.T__5))) != 0):
                        self.state = 80
                        self.listaParams()
                        self.state = 85
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 86
                    self.match(PythonSParser.T__10)
                    self.state = 87
                    self.type_()
                    self.state = 88
                    self.match(PythonSParser.T__11)
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__1) | (1 << PythonSParser.T__2) | (1 << PythonSParser.T__3) | (1 << PythonSParser.T__4) | (1 << PythonSParser.T__5))) != 0):
                        self.state = 89
                        self.decVars()
                        self.state = 94
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PythonSParser.T__8:
                        self.state = 95
                        self.decFunc()
                        self.state = 100
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 102 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 101
                        self.stmt()
                        self.state = 104 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__15) | (1 << PythonSParser.T__18) | (1 << PythonSParser.T__20) | (1 << PythonSParser.T__24) | (1 << PythonSParser.ID))) != 0)):
                            break

                    self.state = 106
                    self.match(PythonSParser.T__12)

                else:
                    raise NoViableAltException(self)
                self.state = 110 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoMainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.StmtContext)
            else:
                return self.getTypedRuleContext(PythonSParser.StmtContext,i)


        def getRuleIndex(self):
            return PythonSParser.RULE_blocoMain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocoMain" ):
                listener.enterBlocoMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocoMain" ):
                listener.exitBlocoMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocoMain" ):
                return visitor.visitBlocoMain(self)
            else:
                return visitor.visitChildren(self)




    def blocoMain(self):

        localctx = PythonSParser.BlocoMainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_blocoMain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PythonSParser.T__8)
            self.state = 113
            self.match(PythonSParser.T__13)
            self.state = 114
            self.match(PythonSParser.T__9)
            self.state = 115
            self.match(PythonSParser.T__10)
            self.state = 116
            self.match(PythonSParser.T__11)
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.stmt()
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__15) | (1 << PythonSParser.T__18) | (1 << PythonSParser.T__20) | (1 << PythonSParser.T__24) | (1 << PythonSParser.ID))) != 0)):
                    break

            self.state = 122
            self.match(PythonSParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_(self):
            return self.getTypedRuleContext(PythonSParser.ForContext,0)


        def doWhile(self):
            return self.getTypedRuleContext(PythonSParser.DoWhileContext,0)


        def if_(self):
            return self.getTypedRuleContext(PythonSParser.IfContext,0)


        def atrib(self):
            return self.getTypedRuleContext(PythonSParser.AtribContext,0)


        def nativeFunc(self):
            return self.getTypedRuleContext(PythonSParser.NativeFuncContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.ID)
            else:
                return self.getToken(PythonSParser.ID, i)

        def operacao(self):
            return self.getTypedRuleContext(PythonSParser.OperacaoContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonSParser.ExprContext,0)


        def NUM(self):
            return self.getToken(PythonSParser.NUM, 0)

        def getRuleIndex(self):
            return PythonSParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = PythonSParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.for_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.doWhile()
                self.state = 126
                self.match(PythonSParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.if_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.atrib()
                self.state = 130
                self.match(PythonSParser.T__0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.nativeFunc()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 133
                self.match(PythonSParser.ID)
                self.state = 134
                self.match(PythonSParser.ID)
                self.state = 135
                self.operacao()
                self.state = 136
                self.match(PythonSParser.ID)
                self.state = 137
                self.match(PythonSParser.T__9)
                self.state = 138
                self.expr(0)
                self.state = 139
                self.match(PythonSParser.T__10)
                self.state = 140
                self.match(PythonSParser.T__0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.match(PythonSParser.ID)
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==PythonSParser.ID or _la==PythonSParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.match(PythonSParser.T__0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 145
                self.match(PythonSParser.ID)
                self.state = 146
                self.match(PythonSParser.T__9)
                self.state = 147
                self.match(PythonSParser.ID)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(PythonSParser.T__10)
                self.state = 150
                self.match(PythonSParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(PythonSParser.StmtContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = PythonSParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_breakStmt)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonSParser.T__15, PythonSParser.T__18, PythonSParser.T__20, PythonSParser.T__24, PythonSParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.stmt()
                pass
            elif token in [PythonSParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(PythonSParser.T__14)
                self.state = 156
                self.match(PythonSParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonSParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonSParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_atrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtrib" ):
                listener.enterAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtrib" ):
                listener.exitAtrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtrib" ):
                return visitor.visitAtrib(self)
            else:
                return visitor.visitChildren(self)




    def atrib(self):

        localctx = PythonSParser.AtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(PythonSParser.ID)
            self.state = 160
            self.match(PythonSParser.T__7)
            self.state = 161
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonSParser.ID, 0)

        def range_(self):
            return self.getTypedRuleContext(PythonSParser.RangeContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(PythonSParser.BreakStmtContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = PythonSParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(PythonSParser.T__15)
            self.state = 164
            self.match(PythonSParser.ID)
            self.state = 165
            self.match(PythonSParser.T__16)
            self.state = 166
            self.match(PythonSParser.T__17)
            self.state = 167
            self.match(PythonSParser.T__9)
            self.state = 168
            self.range_()
            self.state = 169
            self.match(PythonSParser.T__10)
            self.state = 170
            self.match(PythonSParser.T__11)
            self.state = 171
            self.breakStmt()
            self.state = 172
            self.match(PythonSParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def breakStmt(self):
            return self.getTypedRuleContext(PythonSParser.BreakStmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonSParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_doWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhile" ):
                listener.enterDoWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhile" ):
                listener.exitDoWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhile" ):
                return visitor.visitDoWhile(self)
            else:
                return visitor.visitChildren(self)




    def doWhile(self):

        localctx = PythonSParser.DoWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(PythonSParser.T__18)
            self.state = 175
            self.match(PythonSParser.T__11)
            self.state = 176
            self.breakStmt()
            self.state = 177
            self.match(PythonSParser.T__12)
            self.state = 178
            self.match(PythonSParser.T__19)
            self.state = 179
            self.match(PythonSParser.T__9)
            self.state = 180
            self.expr(0)
            self.state = 181
            self.match(PythonSParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonSParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSParser.StmtContext)
            else:
                return self.getTypedRuleContext(PythonSParser.StmtContext,i)


        def getRuleIndex(self):
            return PythonSParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = PythonSParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(PythonSParser.T__20)
            self.state = 184
            self.match(PythonSParser.T__9)
            self.state = 185
            self.expr(0)
            self.state = 186
            self.match(PythonSParser.T__10)
            self.state = 187
            self.match(PythonSParser.T__11)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.stmt()
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__15) | (1 << PythonSParser.T__18) | (1 << PythonSParser.T__20) | (1 << PythonSParser.T__24) | (1 << PythonSParser.ID))) != 0)):
                    break

            self.state = 193
            self.match(PythonSParser.T__12)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PythonSParser.T__21:
                self.state = 194
                self.match(PythonSParser.T__21)
                self.state = 195
                self.match(PythonSParser.T__11)
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 196
                    self.stmt()
                    self.state = 199 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__15) | (1 << PythonSParser.T__18) | (1 << PythonSParser.T__20) | (1 << PythonSParser.T__24) | (1 << PythonSParser.ID))) != 0)):
                        break

                self.state = 201
                self.match(PythonSParser.T__12)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExprContext

        def term(self):
            return self.getTypedRuleContext(PythonSParser.TermContext,0)


        def operacao(self):
            return self.getTypedRuleContext(PythonSParser.OperacaoContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonSParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonSParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonSParser.ExprContext(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    self.operacao()
                    self.state = 210
                    self.term(0)
                    self.state = 211
                    self.match(PythonSParser.T__0) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # TermContext

        def factor(self):
            return self.getTypedRuleContext(PythonSParser.FactorContext,0)


        def operacao(self):
            return self.getTypedRuleContext(PythonSParser.OperacaoContext,0)


        def term(self):
            return self.getTypedRuleContext(PythonSParser.TermContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonSParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonSParser.TermContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    self.operacao()
                    self.state = 223
                    self.factor() 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonSParser.ExprContext,0)


        def ID(self):
            return self.getToken(PythonSParser.ID, 0)

        def NUM(self):
            return self.getToken(PythonSParser.NUM, 0)

        def getRuleIndex(self):
            return PythonSParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = PythonSParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonSParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(PythonSParser.T__9)
                self.state = 231
                self.expr(0)
                self.state = 232
                self.match(PythonSParser.T__10)
                self.state = 234
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 233
                    self.match(PythonSParser.T__0)


                pass
            elif token in [PythonSParser.ID, PythonSParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==PythonSParser.ID or _la==PythonSParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.NUM)
            else:
                return self.getToken(PythonSParser.NUM, i)

        def getRuleIndex(self):
            return PythonSParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = PythonSParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(PythonSParser.NUM)
            self.state = 240
            self.match(PythonSParser.T__22)
            self.state = 241
            self.match(PythonSParser.NUM)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PythonSParser.T__22:
                self.state = 242
                self.match(PythonSParser.T__22)
                self.state = 243
                self.match(PythonSParser.NUM)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PythonSParser.TypeContext,0)


        def ID(self):
            return self.getToken(PythonSParser.ID, 0)

        def listaParams(self):
            return self.getTypedRuleContext(PythonSParser.ListaParamsContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_listaParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParams" ):
                listener.enterListaParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParams" ):
                listener.exitListaParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParams" ):
                return visitor.visitListaParams(self)
            else:
                return visitor.visitChildren(self)




    def listaParams(self):

        localctx = PythonSParser.ListaParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_listaParams)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.type_()
                self.state = 247
                self.match(PythonSParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.type_()
                self.state = 250
                self.match(PythonSParser.ID)
                self.state = 251
                self.match(PythonSParser.T__6)
                self.state = 252
                self.listaParams()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NativeFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonSParser.ID, 0)

        def operacao(self):
            return self.getTypedRuleContext(PythonSParser.OperacaoContext,0)


        def print_(self):
            return self.getTypedRuleContext(PythonSParser.PrintContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_nativeFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNativeFunc" ):
                listener.enterNativeFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNativeFunc" ):
                listener.exitNativeFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNativeFunc" ):
                return visitor.visitNativeFunc(self)
            else:
                return visitor.visitChildren(self)




    def nativeFunc(self):

        localctx = PythonSParser.NativeFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_nativeFunc)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonSParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(PythonSParser.ID)
                self.state = 257
                self.operacao()
                self.state = 258
                self.match(PythonSParser.T__23)
                self.state = 259
                self.match(PythonSParser.T__9)
                self.state = 260
                self.match(PythonSParser.T__10)
                self.state = 261
                self.match(PythonSParser.T__0)
                pass
            elif token in [PythonSParser.T__24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.print_()
                self.state = 264
                self.match(PythonSParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.NUM)
            else:
                return self.getToken(PythonSParser.NUM, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.ID)
            else:
                return self.getToken(PythonSParser.ID, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(PythonSParser.STRING)
            else:
                return self.getToken(PythonSParser.STRING, i)

        def operacao(self):
            return self.getTypedRuleContext(PythonSParser.OperacaoContext,0)


        def getRuleIndex(self):
            return PythonSParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = PythonSParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(PythonSParser.T__24)
                self.state = 269
                self.match(PythonSParser.T__9)
                self.state = 271 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 270
                    _la = self._input.LA(1)
                    if not(_la==PythonSParser.ID or _la==PythonSParser.NUM):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 273 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PythonSParser.ID or _la==PythonSParser.NUM):
                        break

                self.state = 275
                self.match(PythonSParser.T__10)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(PythonSParser.T__24)
                self.state = 277
                self.match(PythonSParser.T__9)
                self.state = 278
                self.match(PythonSParser.STRING)
                self.state = 279
                self.match(PythonSParser.T__6)
                self.state = 280
                _la = self._input.LA(1)
                if not(_la==PythonSParser.ID or _la==PythonSParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                self.operacao()
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==PythonSParser.ID or _la==PythonSParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                self.match(PythonSParser.T__10)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.match(PythonSParser.T__24)
                self.state = 286
                self.match(PythonSParser.T__9)
                self.state = 287
                self.match(PythonSParser.STRING)
                self.state = 288
                self.match(PythonSParser.T__6)
                self.state = 289
                _la = self._input.LA(1)
                if not(_la==PythonSParser.ID or _la==PythonSParser.NUM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 290
                self.match(PythonSParser.T__10)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.match(PythonSParser.T__24)
                self.state = 292
                self.match(PythonSParser.T__9)
                self.state = 293
                self.match(PythonSParser.STRING)
                self.state = 294
                self.match(PythonSParser.T__6)
                self.state = 295
                self.match(PythonSParser.STRING)
                self.state = 296
                self.match(PythonSParser.T__10)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.match(PythonSParser.T__24)
                self.state = 298
                self.match(PythonSParser.T__9)
                self.state = 299
                self.match(PythonSParser.STRING)
                self.state = 300
                self.match(PythonSParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonSParser.RULE_operacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao" ):
                listener.enterOperacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao" ):
                listener.exitOperacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao" ):
                return visitor.visitOperacao(self)
            else:
                return visitor.visitChildren(self)




    def operacao(self):

        localctx = PythonSParser.OperacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSParser.T__7) | (1 << PythonSParser.T__25) | (1 << PythonSParser.T__26) | (1 << PythonSParser.T__27) | (1 << PythonSParser.T__28) | (1 << PythonSParser.T__29) | (1 << PythonSParser.T__30) | (1 << PythonSParser.T__31) | (1 << PythonSParser.T__32) | (1 << PythonSParser.T__33) | (1 << PythonSParser.T__34) | (1 << PythonSParser.T__35) | (1 << PythonSParser.T__36) | (1 << PythonSParser.T__37) | (1 << PythonSParser.T__38) | (1 << PythonSParser.T__39))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        self._predicates[14] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




