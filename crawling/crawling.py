def country_name(x):
    if x == 'U':
        return 'United States of America'
    if x == 'J':
        return 'Japan'
    if x == 'K':
        return 'Korea'
    if x == 'S':
        return 'Switzerland'
    if x == 'UK':
        return 'United Kingdom'
with open('crawling.txt') as f:
    lines = f.readlines()
for i,line in enumerate(lines):
    line = line.replace('\n','')
    if len(line)>5:
        designation = line.split('@',1)[0]
        remaining_d = line.split('@',1)[1]
        country = remaining_d.split('@',1)[0]
        remaining_c = remaining_d.split('@',1)[1]
        country_full_name = str(country_name(str(country)))
        authorName = remaining_c.split('@',1)[0]
        remaining_a = remaining_c.split('@',1)[1]
        photo_link = remaining_a.split('@',1)[0]
        remaining_p = remaining_a.split('@',1)[1]
        societyName = remaining_p
        output = {}
        output['designation'] = designation
        output['authorName'] = authorName
        output['societyName'] = societyName
        temp = list('')
        temp.append(country_full_name)
        output['country'] = temp
        print output
