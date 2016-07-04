import os
import pynotify
def latest_news(data):
    data = data.split('<h2>Latest <span>Stories</span></h2>',1)[1]
    data = data.split('title=',1)[1]
    data = data.split('</a>',1)[0]
    return data
os.system('rm index.php')
os.system('wget www.gulte.com/index.php')
with open('index.php') as f:
    data = f.read()
title = latest_news(data).split('"',1)[1]
title = title.split('"',1)[0]
link = latest_news(data).split('href="',1)[1]
link = link.split('"',1)[0]
pynotify.init("Test")
notice = pynotify.Notification(title, link)
notice.show()
while 1:
    os.system('rm index.php')
    os.system('wget www.gulte.com/index.php')
    with open('index.php') as f:
        data = f.read()
    title_new = latest_news(data).split('"',1)[1]
    title_new = title_new.split('"',1)[0]
    link_new = latest_news(data).split('href="',1)[1]
    link_new = link_new.split('"',1)[0]
    if title_new!=title:
        pynotify.init("Test")
        notice = pynotify.Notification(title_new, link_new)
        notice.show()
