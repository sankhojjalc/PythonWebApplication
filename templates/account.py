from templates import mongoData
class Account():
    name = mongoData.resp['name']
    acc_Num = mongoData.resp['_id']
    mainBalance=mongoData.resp['balance']
    PayeeDetails={}
    datas= mongoData.dataBase    
    def displayName(self):
        return (self.name)
    def displayAcc_Num(self):
        return(self.acc_Num)
    def displayMainBalance(self):
        return (self.mainBalance)
    
    def transferMoney(self,amount,balance):
        check= False
        if(amount>balance):
            return check
        else:
            check=True
            UpdatedBalance=balance-amount
            mongoData.mycol.update(
                {"name":'Sankho'},
                {'$set':{"balance": UpdatedBalance}
                }
            )
   
    def depositMoney(self,amount,balance):
        UpdatedBalance= balance+amount
        mongoData.mycol.update(
            {"name":'Sankho'},
            {'$set':{"balance": UpdatedBalance}
            }
        )
    
    def addPayeeDetails(self,payeeAccountNumber,payeeName):     
      self.PayeeDetails[payeeAccountNumber]=payeeName
      for key,val in self.PayeeDetails.items():
          print('key {} value {}'.format(key,val))

    def removePayeeDetails(self,payeeAccountNumber):
        self.PayeeDetails.pop(payeeAccountNumber,None)
        for key,val in self.PayeeDetails.items():
          print(key,val)