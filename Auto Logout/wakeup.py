import os
os.system('wakeonlan C8:9C:DC:D6:9D:A7 > /dev/null')
print 'Waiting.....'
os.system('ssh nikhil.fulzele@192.168.0.196')