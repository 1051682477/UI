#!/usr/bin/env python

import  os

def path():
	return os.path.dirname(os.path.dirname(__file__))

def filePath(director,fileName):
	return os.path.join(path(), director, fileName)




