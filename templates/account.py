from templates import mongoData
class Account():
    name = mongoData.resp['name']
    acc_Num = mongoData.resp['_id']
    PayeeDetails={}
    datas= mongoData.dataBase    

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
        mongoData.mycol.update(
            {"name": 'Sankho'},
            {'$push':{"addPayee.Added_User_Name": payeeName}},
            upsert=True
        )
        mongoData.mycol.update(
            {"name": 'Sankho'},
            {'$addToSet':{"addPayee.acc_det": payeeAccountNumber}},
            upsert=True
        )    

    def removePayeeDetails(self,name,payeeAccountNumber):
        mongoData.mycol.update(
            {'name': "Sankho"},
            {'$pop':{"addPayee.acc_det": payeeAccountNumber}},
            upsert= True
        )
        mongoData.mycol.update(
            {'name': "Sankho"},
            {'$pop':{"addPayee.Added_User_Name": name}},
            upsert= True
        )