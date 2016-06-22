from gelfclient import UdpClient
from datetime import datetime
from os import listdir
from os.path import isfile, join

gelf_server = 'localhost'

gelf = UdpClient(gelf_server)

gelf = UdpClient(gelf_server, port=12201, mtu=8000, source='ES-server')
#getting the names of all log files in the specified folder
#path = raw_input('Enter the path for log folder here. Eg: /usr/share/elasticsearch/logs/ :')
path = '/home/praneeth/Python-scripts/es-graylog/'
log_files = [f for f in listdir(path) if isfile(join(path, f))]
log_files = filter(lambda f: f.endswith(('.log')), log_files)
old_count = {}
for i,log_file in enumerate(log_files):
    old_count[i] = 0
#function that obtains level from a line
def level(x):
    if 'ERROR' in x:
        return('ERROR')
    if 'INFO' in x:
        return('INFO')
    if 'DEBUG' in x:
        return('DEBUG')
    if 'WARN' in x:
        return('WARN')
#function that converts level name to level number from a line
def level_no(x):
    if 'ERROR' in x:
        return('3')
    if 'INFO' in x:
        return('1')
    if 'DEBUG' in x:
        return('0')
    if 'WARN' in x:
        return('2')
#function that obtains short_message from a line
def short_message(x, y):
    x = x.split(y,1)[1]
    x = x.split('[',1)[1]
    x = x.split(']',1)[0]
    x = x.replace(' ','')
    return x
#function that obtains node name from a line
def node_name(x, y):
    x = x.split(y,1)[1]
    x = x.split('[',1)[1]
    x = x.split(']',1)[0]
    x = x.replace(' ','')
    return x
#function that obtains full from a line
def full_message(x, y):
    x = x.split(y,1)[1]
    x = x.split(']',1)[1]
    x = x.replace('\\',' ')
    return x
#function that obtains timestamp from a line
def timestamp(x):
    x = x.split(']',1)[0]
    x = x.split('[',1)[1]
    x = x.split('[',1)[1]
    x = datetime.strptime(x,"%Y-%m-%d %H:%M:%S,%f")
    b = datetime(1970,1,1)
    return (x-b).total_seconds()-19800
while 1:
    for count,log_file in enumerate(log_files):
        data_position = list('')
        data = list('')
        data_main = {}
        with open(path+log_file) as f:
            lines = f.readlines()
        for i,line in enumerate(lines):
            if i>int(old_count[count]):
                if line[0] == '[':
                    data.append('')
                    data_position.append(i)
                    old_count[count] = i
        for i,x in enumerate(data_position):
            try:
                data[i] = lines[int(x):][:int(data_position[i+1])-int(x):]
            except:
                data[i] = lines[int(x):]
        for i,value in enumerate(data):
            data_main[i] = {}
            data_main[i]['level'] = level(str(value))
            data_main[i]['short_message'] = short_message(str(value),str(data_main[i]['level']))
            data_main[i]['node_name'] = node_name(str(value),str(data_main[i]['short_message']))
            data_main[i]['timestamp'] = timestamp(str(value))
            data_main[i]['level'] = level_no(str(value))
            data_main[i]['full_message'] = full_message(str(value),str(data_main[i]['node_name']))
        for i in range(0,len(data_main)):
            gelf.log(data_main[i])
