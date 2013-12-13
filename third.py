movies = ["taitannikehao",1969,"sejie",2010,
           ["The mean of life",2012,"spring","yini"]]

def print_lol(the_list,level):
    for the_item in the_list:
        if isinstance(the_item,list):
           print_lol(the_item,level+1)
        else:
           for tab_stop in range(level):
               print("\t")
           print(the_item)

print_lol(movies,2)
