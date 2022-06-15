import webbrowser
from fpdf import FPDF

class Bill:
    #object that contain data about a bill,such as
    #total amount and period of the Bill
    
    def __init__(self,amount,period):
        self.amount=amount,
        self.period=period

class Flatmate:

    # creat a flatmate person who lives in the flat
    # and pay a share of the bill

    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house=days_in_house 


    def pays(self,bill,flatmate2):
        weight= self.days_in_house/(self.days_in_house+flatmate2.days_in_house) 
        to_pay=bill.amount*weight
        return to_pay  

class PdfReport:
    # creat a pdf file that contain data about
    # the flatmate such as thie name,thie due amounts
    # and period of the bill.days_in_house 

    def __init__(self,flatmate):
        self.flatmate=flatmate   

    def generate(self,flatmate1,flatmate2,bill):
        flatmate1_pay=str(round(flatmate1.pays(bill,flatmate2), 2))
        flatmate2_pay=str(round(flatmate2.pays(bill,flatmate1), 2)) 

        pdf=FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()  

        #add icon
        pdf.set_font(family='Time',size=24, style='B')
        pdf.cell(w=8,h=88, txt='Flatmate Bill', border=0,align='C',ln=1) 

        #insert period label and value 
        pdf.set_font(family='Time',size=24,style='B')
        pdf.cell(w=100,h=25,txt=flatmate1.name,border=0)
        pdf.cell(w=150,h=25,txt=flatmate1_pay,border=0, ln=1)  

        #insert name and due amounts of the first flatmate 
        pdf.cell(w=100,h=25,txt=flatmate2.name,border=0)
        pdf.cell(w=150,h=25,txt=flatmate2_pay,border=0, ln=1)   
         pdf.output(self,filename)  
         webbrowser.open(self,filename)  
        
amount=float(input('Hi user,enter the bill amount: ')) 
period=int(input('What is the bill period? E.g April 2021: '))

name1=input('What is your name? ')
days_in_house1=int(input(f'How many days did {name1} stay in the house during the bill period? ')
                   
name2=input('What is the name of the other flatmate? ')
days_in_house2=int(input(f'How many days did {name2} stay in the house during the bill period? ')                   

the_bill=Bill(amount,period)
flatmate1=Flatmate(name1,days_in_house1)
flatmate2=Flatmate(name2,days_in_house2)
                   
print(f'{flatmate1.name} pays:' ,flatmate1.pays(the_bill,flatmate2))
print(f'{flatmate2.name} pays:' ,flatmate2.pays(the_bill,flatmate1))

pdf_report=PdfReport(filename=f'{the_bill,period}.pdf')
pdf_report.generate=(flatmate1,flatmate2,the_bill)
