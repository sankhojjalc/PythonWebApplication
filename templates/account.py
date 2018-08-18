from templates import mongoData
class Account():
    name = ""
    acc_Num = ''
    mainBalance=0
    PayeeDetails={}  
    
    def __init__(self, name,acc_Num,mainBalance):
        self.name=name
        self.acc_Num=acc_Num
        self.mainBalance=mainBalance
    
    def displayName(self):
        return (self.name)
    def displayAcc_Num(self):
        return(self.acc_Num)
    def displayMainBalance(self):
        return (self.mainBalance)
    
    def transferMoney(self,amount):
        error= None        
        if(amount>self.mainBalance):
            error= 'Insufficient Balance'
        else:
           self.mainBalance-=amount
    
    def depositMoney(self,amount):
        self.mainBalance+=amount
    
    def addPayeeDetails(self,payeeAccountNumber,payeeName):     
      self.PayeeDetails[payeeAccountNumber]=payeeName
      for key,val in self.PayeeDetails.items():
          print('key {} value {}'.format(key,val))

    def removePayeeDetails(self,payeeAccountNumber):
        self.PayeeDetails.pop(payeeAccountNumber,None)
        for key,val in self.PayeeDetails.items():
          print(key,val)