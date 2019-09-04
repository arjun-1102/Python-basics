class ReversedStr(str):
	def __new__(*args, **kwargs):
		self = str.__new__(*args, **kwargs)
		self = self[::-1]
		return self
		
#from reversedString import ReversedStr
#test_one = ReversedStr("Try this once")
#test_one


	
