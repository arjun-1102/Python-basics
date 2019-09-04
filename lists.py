

shopping_list = []

def show_help():
	print("What should we pick up at the store?")
	print("""
	Enter 'DONE' to stop adding items.
	Enter 'HELP' for this help.
	Enter 'SHOW' to view current list.
	""")

def add_to_list(item):
	shopping_list.append(item)
	print("Added {} to the list. {} items in list.".format(item, len(shopping_list)))
#	return shopping_list

def show_list():
	print("Here's your list")
	for i in shopping_list:
		print(i)
	
show_help()

while True:	
	new_item = input("> ")
	
	if new_item == 'DONE':
		break
	elif new_item =='HELP':
		show_help()
		continue
	elif new_item =='SHOW':
		show_list()
		continue
	add_to_list(new_item)

show_list()