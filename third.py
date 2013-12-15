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


