from gelfclient import UdpClient
from datetime import datetime
gelf_server = 'localhost'

# Using mandatory arguments
gelf = UdpClient(gelf_server)

# Using all arguments
gelf = UdpClient(gelf_server, port=12201, mtu=8000, source='ES-server')

def level(x):
    if 'ERROR' in x:
        return('ERROR')
    if 'INFO' in x:
        return('INFO')
    if 'DEBUG' in x:
        return('DEBUG')
    if 'WARN' in x:
        return('WARN')
def level_no(x):
    if 'ERROR' in x:
        return('3')
    if 'INFO' in x:
        return('1')
    if 'DEBUG' in x:
        return('0')
    if 'WARN' in x:
        return('2')
def short_message(x, y):
    x = x.split(y,1)[1]
    x = x.split('[',1)[1]
    x = x.split(']',1)[0]
    x = x.replace(' ','')
    return x
def node_name(x, y):
    x = x.split(y,1)[1]
    x = x.split('[',1)[1]
    x = x.split(']',1)[0]
    x = x.replace(' ','')
    return x

def full_message(x, y):
    x = x.split(y,1)[1]
    x = x.split(']',1)[1]
    return x

def timestamp(x):
    x = x.split(']',1)[0]
    x = x.split('[',1)[1]
    x = x.split('[',1)[1]
    x = datetime.strptime(x,"%Y-%m-%d %H:%M:%S,%f")
    b = datetime(1970,1,1)
    return (x-b).total_seconds()
data_position = list('')
data = list('')
data_main = {}
with open('a.log') as f:
    lines = f.readlines()

for i,line in enumerate(lines):
    if line[0] == '[':
        data.append('')
        data_position.append(i)
#print len(data)
#print len(data_position)
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
