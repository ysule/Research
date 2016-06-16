list_names = list('')
with open('tp.txt') as f:
    names = f.readlines()
for name in names:
    name = name.split('"',1)[1]
    name = name.split('"',1)[0]
    if len(name)>30:
        list_names.append(name)
    else:
        for letter in name:
            if letter not in 'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM':
                list_names.append(name)
print list_names
