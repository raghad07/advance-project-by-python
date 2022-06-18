from flat import Bill,Flatmate
from reports import PdfReport,FileShare

amount=float(input("Hey user,enter the bill amount : "))
period=str(input("What is the bill priopd? E.g. May 2022: "))

name1=str(input("what is your name? "))
days_in_house1=int(input(f'How many days did {name1} stay in the house during the bill period?  '))

name2=str(input("what is the name of the other flatmate? "))
days_in_house2=int(input(f'How many days did {name2} stay in the house during the bill period? '))

the_bill=Bill(amount=amount,period=period)  
Flatmate_1=Flatmate(name=name1,days_in_house=days_in_house1) 
Flatmate_2= Flatmate(name=name2,days_in_house=days_in_house2) 

print(f'{Flatmate_1.name} pays: ' ,Flatmate_1.pays(bill=the_bill,flatmate2=Flatmate_2))
print(f'{Flatmate_2.name} pays: ',Flatmate_2.pays(bill=the_bill,flatmate2=Flatmate_1))

pdf_report=PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1=Flatmate_1, flatmate2=Flatmate_2, bill=the_bill)

file_share=FileShare(filepath=pdf_report.filename)
print(file_share.share())