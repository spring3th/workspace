movies = ["taitannikehao",1969,"sejie",2010,
           ["The mean of life",2012,"spring","yini"]]

def print_lol(the_list):
    for the_item in the_list:
        if isinstance(the_item,list):
           print_lol(the_item)
        else:
           print(the_item)

print_lol(movies)
