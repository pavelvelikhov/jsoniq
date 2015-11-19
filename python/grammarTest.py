import sys
from antlr4 import *
from jsoniqLexer import jsoniqLexer
from jsoniqParser import jsoniqParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = jsoniqLexer(input)
    stream = CommonTokenStream(lexer)
    parser = jsoniqParser(stream)
    tree = parser.program()
 
if __name__ == '__main__':
    main(sys.argv)
