from fpdf import FPDF
import webbrowser
from flat import Bill,Flatmate
from filestack import Client

class PdfReport:

    """creat a pdf file that contain data about
    the flatmate such as thie name,thie due amounts
    and period of the bill.days_in_house """


    def __init__(self,filename):
        self.filename=filename


    def generate(self,flatmate1,flatmate2,bill):
        flatmate1_pay=str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate2_pay=str(round(flatmate2.pays(bill,flatmate1),2))

        pdf=FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()
        
         #add icon
        pdf.set_font(family='Arial',size=24,style='B')
        pdf.cell(w=500,h=40,txt='Flatemate Bill',border=1,align='C',ln=1)

        #insert period label and value 
        pdf.set_font(family='Arial',size=14,style='B')
        pdf.cell(w=200,h=50,txt='Period: ',)
        pdf.cell(w=100,h=50,txt=bill.period,ln=1)
        
        #insert name and due amounts of the first flatmate 
        pdf.set_font(family='Arial',size=12)
        pdf.cell(w=200,h=50,txt=flatmate1.name)
        pdf.cell(w=100,h=50,txt=flatmate1_pay,ln=1)

        pdf.cell(w=200,h=50,txt=flatmate2.name)
        pdf.cell(w=100,h=50,txt=flatmate2_pay)

        
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class FileShare:

    def __init__(self, filepath,api_key="AMNGylatVRmugCEGE5Yqhz"):
        self.filepath=filepath
        self.api_key=api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url           