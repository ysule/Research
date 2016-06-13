import os
#getting the names of all pdf files in the current folder
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = filter(lambda f: f.endswith(('.pdf')), files)
for pdf_file in files:
    #checking and creating html file for pdf file if html file is not there
    html_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    html_files = filter(lambda f: f.endswith(('.html')), html_files)
    html_file = pdf_file.replace('.pdf','') + '.html'
    if html_file not in html_files:
        os.system("pdf2txt.py -o " + pdf_file.replace('.pdf','') + '.html -t html '+pdf_file)
#getting the html files names (in the folder) after generating html files for pdfs
html_files = [f for f in os.listdir('.') if os.path.isfile(f)]
html_files = filter(lambda f: f.endswith(('.html')), html_files)
for html_file in html_files:
    with open(html_file) as f:
        lines = f.readlines()
        f.close()
    """
    with open(html_file) as f:
        all_lines = f.read()
        f.close()
    """
#finding the element with max font size in the first 30 lines and extracting title from it.
    font_size_old = 0
    for i,line in enumerate(lines):
        if i<30:
            if 'font-size:' in line:
                x = line.split("font-size:",1)[1]
                font_size_new = int(x.split("px",1)[0])
                if font_size_new > font_size_old:
                    title = line.rsplit('">', 1)[-1].replace("\n","")
                    font_size_old = font_size_new
    if title:
        print 'title: '+title
    """
    if 'abstract' in all_lines.lower():
        x = all_lines.split("Abstract",1)[1]
        y = x.split("style",1)[1]
        z = y.split("style",1)[0]
    if z:
        print 'abstract version of abstract is ' + z
    """
