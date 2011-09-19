"""
	This file contains the implementation of CacheBlock.
	Each cache block stores the state of block i.e whether
	it is in M or E or S or I state.

	Here we assume the size of cache block is 64 Bytes 
"""

class CacheBlock:
	
	# constructor
	def __init__(self, state):
		self._state    = state;
		self._lruCount = 1000;

	def ChangeState(self, state):
		self._state = state;

	def GetState(self):
		return self._state;

	def GetLfuCount(self):
		return self._lfuCount;

	def DecrementLFU(self):
		self._lruCount = self._lruCount - 1;
#------------------ end of class "CacheBlock" ----------------------#
