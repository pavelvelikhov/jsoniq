## Lets try to build a simple JSONiq query processor
The spec is here: http://www.jsoniq.org/

The plan:
 1. Build ANTLR grammar, publish it on the ANTLR site
 2. Build a prototype processor in Python3 w/o any XQuery functions or advanced operations
 3. Build a Java or Scala processor
 4. Add in functions from SAXON
 5. Add schema features

===================

Current status: Basic grammar working, except for update syntax and comment syntax

Project is discontinued, all efforts shifter towards pythonql
