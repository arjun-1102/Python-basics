import copy
class FilledList(list):
	def __init__(self, count, value, *args, **kwargs):
		super().__init__()
		for _ in range(count):
			self.append(copy.copy(value))
			
#import filledlist
#fl = filledlist.FilledList(9,2)
#len(fl)
#fl
#fl2 = filledlist.FilledList(2, [1,2,3])
#fl2
#fl2[0][1] = 5
#fl2
