movies = ["taitannikehao",1969,"sejie",2010,
           ["The mean of life",2012,"spring","yini"]]

def print_lol(the_list,indent=False,level=0):
	for the_item in the_list:
		if isinstance(the_item,list):
			print_lol(the_item,indent,level+1)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t",end='')
			print(the_item)

print_lol(movies,True,2)
