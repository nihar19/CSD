"""
	This module contains the implmentation of MESI protocol.
"""

class MESI:
	
	def __init__(self):
		pass;
	
	"""
		signal is the request either from processor (or) bus side.

		output is a list, where first entry is the final state followed by
		the output signal.
	"""
	def GetOutput(self, currentState, signal):
		if(currentState == 'M'):
			return self.__GetOutputFromModified(signal);

		elif(currentState == 'E'):
			return self.__GetOutputFromInvalid(signal);

		elif(currentState == 'S'):
			return self.__GetOutputFromShared(signal);

		elif(currentState == 'I'):
			return self.__GetOutputFromInvalid(signal);

		# invalid
		return [];

	"""
		Returns the outputs, when the cacheBlock is
		present in Modified state.
	"""
	def __GetOutputFromModified(self, signal):
		
		# if signal is BusRdX or BusRd
		if(signal == 'BX' or signal == 'BR'):
			return ['M','F'];

		# if signal is ProcessorRead or ProccesorWrite
		elif(signal == 'PR' or signal == 'PW'):
			return ['M'];

		# invalid
		return [];

	"""
		Returns the outputs, when the cacheBlock is
		present in Invalid state.

		NOTE: When a cacheBlock is currently in Invalid state,
			  recieves ProcessorRead signal, then BusRd signal
			  is outputed but, the state transition further depends
			  on whether Shared bit is asserted or not, this has
			  to be taken care by the CacheController.py
	"""
	def __GetOutputFromInvalid(self, signal):

		# if signal is ProcessorRead.
		if(signal == 'PR'):
			return ['D','BR']; 
		
		# if signal is ProcessorWrite.
		elif(signal == 'PW'):	
			return ['M','BX'];

		# invalid
		return [];

	"""
		Returns the outputs, when the cacheBlock is
		present in Exclusive state.
	"""
	def __GetOutputFromExclusive(self, signal):
		
		# if signal is ProcessorRead.
		if(signal == 'PR'):
			return ['E'];

		# if signal is ProcessorWrite
		elif(signal == 'PW'):
			return ['M'];

		# if signal is BusRd.
		elif(signal == 'BR'):
			return ['S','F'];
		
		# if signal is BusRdX.
		elif(signal == 'BX'):
			return ['I','F'];

		# invalid
		return [];

	"""
		Returns the outputs, when the cacheBlock is
		present in Shared state.
	"""
	def __GetOutputFromShared(self, signal):
		
		# if signal is ProcessorRead.
		if(signal == 'PR'):
			return ['S'];

		# if signal is ProcessorWrite.
		elif(signal == 'PW'):
			return ['M','BX'];

		# if signal is BusRdX.
		elif(signal == 'BX'):
			return ['I','F'];

		# if signal is BusRd.
		elif(signal == 'BR'):
			return ['S','F'];

		# invalid
		return [];

#------------------ end of class "MESI" ----------------------#
