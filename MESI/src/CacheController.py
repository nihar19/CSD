"""
	This module implements cacheController which takes of any
	requests appearing either on the bus or by the processor,
	serves the request.

	The main module needs to have four instances of the cacheController
	one for each core.
"""

import Cache;

class CacheController:

	def __init__(self):
		self._cache    = Cache();	
		self._automata = MESI();

	"""
		this handles read requests from processor, outputs 
		the bus transaction to be done(if any).

		A read request will generate bus transactions only when 
		the cacheBlock is in Invalid state or there is a cache miss.
		In such case the processor issues BusRdX signal, 
		and then depending on the response on the bus changes state.
		i.e., there are three stages in this operation as:
		1. cacheController generating txn on the bus. 
		2. other cacheControllers snooping the bus, place response.
		3. cacheController takes action based on response.
		(This has to be taken care by main module)
	"""
	def ProcessorRead(self, setId, tag):

		state = self._cache.GetState(setId, tag);

		# cache hit
		if(len(state) == 1 and state[0] != 'I'):
			mesiTxn = self._automata.GetOutput(state[0],request);
			self._cache.ChangeState(setId, tag, mesiTxn[0]);
			return [];

		# cache miss or cacheBlock in Invalid state
		else:
			mesiTxn = self._automata.GetOutput(state[0],request);
			return ['BR','ThisIsPeculiarCase'];

	"""
		this handles write requests from processor, outputs 
		the bus transaction to be done(if any).
	"""
	def ProcessorWrite(self, setId, tag):
		mesiTxn = self._automata.GetOutput(state[0],request);
		self._cache.ChangeState(setId, tag, mesiTxn[0]);
				
		if(len(mesiTxn) == 2):
			return [mesiTxn[1]];

		return [];
		
	"""
		this handles any request appearing on the bus,
		outputs the response to the request.
	"""
	def BusRequest(self, setId, tag, request):
		return ProcessorWrite(setId, tag);
