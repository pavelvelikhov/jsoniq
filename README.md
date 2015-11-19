## Lets try to build a simple JSONiq query processor
The spec is here: http://www.jsoniq.org/

The plan:
 1. Build ANTLR grammar, build a prototype processor in Python3 w/o any XQuery functions
 2. Build a Java processor
 3. Add in functions from SAXON
 4. Add schema features

===================

Current status: Basic grammar working, except for update syntax and comment syntax
