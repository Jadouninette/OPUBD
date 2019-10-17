import PyPDF2

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = PyPDF2.PdfFileReader(open(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    name = os.path.basename(path)
    name = ' '.join(name.split(' ')[:-1])
    fichier = open(name+".txt","x",encoding='utf-8')
    fichier.write(content)
    fichier.close()

    return
    

