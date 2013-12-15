"""
author:spring
author_email:dengchagnqing@gmail.com
sit:www.ssjike.com
"""
#list opration
movies = ["taitannikehao",1969,"sejie",2010,
           ["The mean of life",2012,"spring","yini"]]
#genju tiaojian lai xunfan bianli list
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

#==========================
"""import导入包,open()BIF打开一个磁盘文件，创建一个迭代器从文件读取数据，一次读取一个数据行。
readline()从打开的文件读取一行数据。seek()可以用来将文件退回到起始位置。close()关闭一个之前打开的文件。
split()方法可以将一个字符串分解为一个子串列表。"""
import os
print(os.getcwd())#返回当前目录
#切换到指定目录
#os.chdir('../home/software')
#对异常进行处理
try:
    data = open('text.txt')
    for each_line in data:
        try:    
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print('said:',end='')
            print(line_spoken,end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print(data.readline(),end='')


