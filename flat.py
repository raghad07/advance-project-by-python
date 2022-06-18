class Bill:
    """object that contain data about a bill,such as
    total amount and period of the Bill"""

    def __init__(self,amount,period):

        self.amount=amount
        self.period=period

class Flatmate:
    """creat a flatmate person who lives in the flat
    and pay a share of the bill"""

    
    def __init__(self,name,days_in_house):
        self.name=name
        self.days_in_house=days_in_house

    def pays(self,bill,flatmate2):

        weight= self.days_in_house/(self.days_in_house+flatmate2.days_in_house) 
        to_pay=bill.amount*weight
        return to_pay 
        


