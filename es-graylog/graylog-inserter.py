from gelfclient import UdpClient

gelf_server = 'localhost'

# Using mandatory arguments
gelf = UdpClient(gelf_server)

# Using all arguments
gelf = UdpClient(gelf_server, port=12202, mtu=8000, source='macbook.local')

# Bare minimum is to send a string, which will map to gelf['short_message']
gelf.log('server is DOWN')

# 'source' and 'host' are the same. Defaults to socket.gethostname() but can be overridden
gelf.log('server is DOWN', source='hostchecker')

# Set extra fields
gelf.log('status change', _state='DOWN', _server='macbook')

# Set severity level
import syslog
gelf.log('unexpected error', level=syslog.LOG_CRIT)

# You can also prepare all data into a dictionary and give that to .log
data = {}
data['short_message'] = 'warning from python'
data['host'] = 'hostchecker'
data['level'] = syslog.LOG_WARNING
gelf.log(data)
