class JavaScriptObject(dict):
	def __getattribute__(self, item):
		try:
			return self[item]
		except KeyError:
			return super().__getattribute__(item)
			
#import javascriptobject
#jso = javascriptobject.JavaScriptObject({'name':'Arjun'})
#jso.language = 'Python'
#jso.name
#jso.language