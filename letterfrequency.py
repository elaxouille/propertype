#!/usr/bin/python

### http://rosettacode.org/wiki/Letter_frequency#Using_collections.Counter
import collections, sys

def letterfrequency(openfile):
	return sorted(collections.Counter(c for l in openfile for c in l).items())