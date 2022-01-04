#pip install pyPDF2

import os 
from PyPDF2 import PdfFileMerger

source_dir = os.getcwd()


merger = PdfFileMerger()      # object for pdffilehandler

for item in os.listdir(source_dir):      #  mergingi all the system and signal pdfs

    if item.endswith('.pdf'):               # take all the file ending with pdf 
        merger.append(item)
    
merger.write('./output/lecturecomplete.pdf')        #writing the object in final pdf 
merger.close()     #ctrl+B to run the code
# this is one of the method to use pyPDF2 function there are a lot of diffrent method to read and write file and merging