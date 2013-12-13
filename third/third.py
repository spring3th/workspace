#author :springdeng
"""递归输出列表，建立函数递归查找，打印输出"""
movies = ["taitannikehao",1969,"sejie",2010,
           ["The mean of life",2012,"spring","yini"]]

def print_lol(the_list):
    for the_item in the_list:
        if isinstance(the_item,list):
           print_lol(the_item)
        else:
           print(the_item)
#调用函数，传递参数
print_lol(movies)
