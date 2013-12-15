import pickle

man = []
other = []
try:
    data = open('text.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'spring':
                man.append(line_spoken)
            elif role == '邓佩瑶':
                other.append(line_spoken)# print('邓佩瑶:',line_spoken)
        except ValueError:
            pass
except IOError as err:
    print('File error:'+str(err))#str()强制将对象转换成字符串形式

try:
    man_file = open('man_file.txt','w')
    other_file = open('other_file.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
   
except IOError:
    print('File error')
finally:
    #locals()返回当前作用域定义的所有名的一个集合。
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()
        
#======================
try:
    with open('man_file.txt','w') as man_file,open('other_file.txt','w') as other_file:
        print(man,file=man_file)
        print(other,file=other_file)
except IOError as err:
        print('File error:'+str(err))
        
#=============================================


try:
    with open('man_file.txt','wb') as man_file,open('other_file.txt','wb') as other_file:#wb是以二进制的形式写入文件
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except pickle.PickleError as perr:
    print('pickling error:'+str(perr))
    
new_man = []
new_other = []
try:
    with open('man_file.txt','rb') as man_file,open('other_file.txt','rb') as other_file:#以二进制的形式读取文件
        new_man = pickle.load(man_file)
        new_other = pickle.load(other_file)
        print(new_man)
        print(new_other)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('pickling error:'+str(perr))

"""将不同方式表示的时间间隔进行统一处理成点号分割的时间"""
def sanitize(time_string):
    if '-' in time_string:#-是否包含在字符串
        splitter = '-'
    elif ':' in time_string:#：是否包含在字符串
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

with open('james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(',')
print(james)
print(sorted(james))

clean_james = []
#迭代处理每个以逗号分割的时间，按格式化成点号分割。
for each_t in james:
    clean_james.append(sanitize(each_t))
print(sorted(clean_james,reverse=True))#从大到小排序，默认是从小到大排序

#列表推导
clean_mikey = [sanitize(each_t) for each_t in james]
print('-------------------------------------------')
print(sorted(clean_mikey))
print(sorted(clean_mikey,reverse=True))

mins = [1,2,3]
secs = [m*60 for m in mins]
print(secs)

meters = [1,10,3]
feet = [m*3.281 for m in meters]
print(feet)

lower = ["I","don't","like","spam"]
upper = [s.upper() for s in lower]
print(upper)
"""列表推导简洁，优雅，代码少"""
print('===================================')
james_sort = sorted([sanitize(each_t) for each_t in james])
unique_james = []
for each_t in james_sort:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])#分片取列表0～2不包括3在内。如果从后向前，则包括

"""Python中集合（set()）最突出的特性是集合中的数据项是无序的，而且不允许重复。如果试图
向一个集合增加一个数据项，而且该集合中已经包含友这个数据项，python就会直接将其忽略。"""
distances = set()
distances ={10.6,11,8,10.6,"two",7}#相同数据直接忽略
distances = set(james)#相同数据直接忽略

print(sorted(set([sanitize(each_t) for each_t in james]))[0:3])
"""以上代码从里往外读，先each_t是否包含在james，然后调用函数进行转换成统一的格式输出。
然后返回列表建立集合，根据集合的特性去掉重复的数据项，最后排序列表，分片取前三，输出到屏幕"""

                        
                