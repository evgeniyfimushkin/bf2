#! /usr/bin/python
#
# lowercaseDir.py <path>
#
# Lower-cases an entire hierachy of directories starting from <path>.
# The case of python-files is not changed.
# Author: Andreas Fredriksson (andreas.fredriksson@dice.se)
# Modified by: Andreas Andersson (andreas.andersson@dice.se)
# Copyright (c)2005 Digital Illusions

import sys
import os
import os.path

class Arguments:
	verbose = 0
	superVerbose = 0
	pretend = 0

def visit(args, dirname, names):
	if args.superVerbose:
		print "entering", dirname
	
	newNames = []
	for x in names:
		if x.endswith('.py'):
				if args.superVerbose:
					print "Skipping .py-file " + x
				continue
		low = x.lower()
		if low != x:
			if args.verbose:
				print "renaming:", x, "to", low
			if not args.pretend:
				os.rename(os.path.join(dirname, x), os.path.join(dirname, low))
			
		if os.path.isdir(os.path.join(dirname, low)):
			newNames.append(low)
	
	if not args.pretend:
		names[:] = newNames

def printUsage():
	print "usage: lowercaseDir.py <dir> [--verbose] [--pretend] [--superVerbose]"

args = Arguments()
args.verbose = 0
args.superVerbose = 0
args.pretend = 0
directory = None
for arg in sys.argv[1:]:
	if arg == "--pretend":
		args.pretend = 1
	elif arg == "--verbose":
		args.verbose = 1
	elif arg == "--superVerbose":
		args.superVerbose = 1
	else:
		directory = arg

if directory != None:
	os.path.walk(directory, visit, args)
else:
	printUsage()
	



