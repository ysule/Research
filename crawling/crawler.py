import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.authors
def country_name(x):
    if x == 'U':
        return 'Uganda'
    if x == 'T':
        return 'Turky'
    if x == 'S':
        return 'Spain'
    if x == 'A':
        return 'Argentina'
    if x == 'N':
        return 'Netherlands'
    if x == 'G':
        return 'Germany'
    if x == 'NZ':
        return 'New Zeland'
    if x == 'SW':
        return 'Switzerland'
    if x == 'AS':
        return 'Australia'
    if x == 'US':
        return 'United States of America'
    if x == 'C':
        return 'Canada'
with open(raw_input("Enter text file name:")) as f:
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
        output['imageLink'] = photo_link
        temp = list('')
        temp.append(country_full_name)
        output['country'] = temp
        db.authors.insert(output)
