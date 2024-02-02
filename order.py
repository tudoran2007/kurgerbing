class Order():
    def __init__(self, name, ordernumber, price, tablenumber):
        self.name = name
        self.ordernumber = ordernumber
        self.price = price
        self.tablenr = tablenumber
    
    def getorderinfo(self):
        return self.name+" ordered "+self.ordernumber+" which costs "+str(self.price)