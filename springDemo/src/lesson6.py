class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    
    
a = Athlete('spring')
b = Athlete('hufang','19810213',['2:23','2-13','4.45'])

print(a.name)
print(b.name)
print(type(a))
    

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

def  get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            #return(data.strip().split(','))
            """return({'Name':templ.pop(0),
                    'DOB':templ.pop(0),
                    'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})"""
            return(Athlete(templ.pop(0)),templ.pop(0),templ)
    except IOError as ioerr:
            print('File error:'+str(ioerr))
            return(None)
        
sarah = get_coach_data('sarah.txt')
print(type(sarah))

#(saah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)#pop(0)调用将删除并返回最前面的数据项，两个pop(0)则删除前两个数据项
#print(sarah_name+"'s fastes times are:"+str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
    
"""创建两个空字典，一个使用大括号创建，另一个用工厂函数来创建
cleese = {},palin = dict()
type(cleese) 输出对象类型，字典通过值与键关联"""

"""sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name']+"'s fastest times are:"+str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
"""
#print(sarah['Name']+"'s fastest times are:"+sarah['Times'])
print(sarah.name+"'s fastest times are:"+str(sarah.top3()))

