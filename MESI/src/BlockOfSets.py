"""
	This file contains the implementation for
	each of the block i.e here since the cache is
	4-way set associative we need 4 instances of the
	BlockOfSets.

	Each BlockOfSets contain one data item for each
	of the 64 sets present.
"""

import CacheBlock;

"""
	Details of implementation:(blocks in sets) 

						We maintain two dictionaries
	each for tagMemory & dataMemory, where each dictionary 
	contianing max of 64 keys.
	
	1. For tagMemory key is the set identifier & value is the tag.

	2. For dataMemory key is the set identifier & value is the 
	object(or instance) of CacheBlock.
"""
class BlockOfSets:

	# constructor
	def __init__(self):
		self._tagMemory  = {};
		self._dataMemory = {};

	"""
		if there is an entry corresponding
		to the setId then return a list 
		containing tag, else return empty list.
	"""
	def GetTag(self, setId):
		if(self._tagMemory.has_key(setId)):
			return [self._tagMemory[setId]];

		return [];

	"""
		if the key setId already exists in the self._tagMemory
		dictionary then reassign the value, return true.
		
		else if the number of keys already present in dictionary < 64, 
		then create a new entry, return true.

		else return false, since we cant create new entry.
	"""
	def SetValue(self, setId, tag, state):
		if(self._tagMemory.has_key(setId)): 
			self._tagMemory[setId] = tag;
			del self._dataMemory[setId];
			self._dataMemory[setId] = CacheBlock(state);
			return True;

		elif( len(self._tagMemory.keys()) < 64) ):
			self._tagMemory[setId] = tag;
			self._dataMemory[setId] = CacheBlock(state);
			return True;

		return False;

	"""
		change state of the cacheBlock.
	"""
	def ChangeState(self, setId, tag, state):
		if(self._tagMemory.has_key(setId) and self._tagMemory[setId] == tag):
			self._dataMemory[setId].ChangeState(state);

	"""
		if the tag is present in this blocks of sets, then return the list
		containing the state of CacheBlock corresponding to it.

		else, return an empty list.
	"""
	def GetData(self, setId, tag):
		if(self._tagMemory.has_key(setId) and self._tagMemory[setId] == tag):
			return [self._dataMemory[setId].GetState()];
		return [];

	"""
		Get lru count of the cacheBlock.
	"""
	def GetLfuCount(self, setId):
		if(self._tagMemory.has_key(setId)):
			return self._dataMemory[setId].GetLfuCount();

		return -1;

	"""
		Decrement lru count of the cacheBlock.
	"""
	def DecrementLFU(self, setId, tag):
		if(self._tagMemory.has_key(setId) and self._tagMemory[setId] == tag):
			self._dataMemory[setId].DecrementLFU();
#------------------ end of class "BlockOfSets" ----------------------#
