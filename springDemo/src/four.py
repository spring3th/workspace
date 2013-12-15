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
                other.append(line_spoken)
                print('邓佩瑶:',line_spoken)
        except ValueError:
            pass
except IOError:
    print('The datafile is missing!')

try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
    man_file.close()
    other_file.close()
except IOError:
    print('File error')

                