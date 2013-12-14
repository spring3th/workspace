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
print(os.getcwd())#fan hui dangqian mulu
#qie huan dao zhiding mulu 
#os.chdir('../home/software')

data = open('test.txt')

data.seek(0)#wenjian qishi
for each_line in data:
	(role,line_spoken) = each_line.split(':',1)
	print(role,end='')
	print('said:',end='')
	print(line_spoken,en='')
data.close()
#print(data.readline(),end='')


