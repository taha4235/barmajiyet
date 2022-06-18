import pdfkit
import os
pdfile = "C:\taha file(x86)\\whkdfjfjdd\\"
config = pdfkit.configuration(wkhtmltopdf = pdffile)
pdfkit.from_url("www.google.com","saveffile.pdf" configuration=config)
os.startfile("savefile.pdf")
url = input("enter url site:")
