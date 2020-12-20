from sploitkit import *
import os

class test(Module):
	""" Description here 

	Author:  your name (your email)
	Version: 1.0
	"""
	def run(self):
		print('test')
		pass

	def ls(self):
		print('ls')
		os.ls()
		pass
