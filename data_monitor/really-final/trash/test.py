with open('servers.txt') as f:
	servers = f.readlines()

for server in servers:
	server = server.replace("\n", "")
	print server