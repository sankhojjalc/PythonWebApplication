import pymongo
def mongoPythonConnection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    dataBase=[
        { "_id": 1,
            "name": "Sankhojjal", 
            "password": 1234,
            "balance": 100000,
            "addPayee": {
                "name": "Podu",
                "acc_det": 2000
            }},
            { "_id": 2,
            "name": "Prateek", 
            "password": 1234,
            "balance": 100000,
            "addPayee": {
                "name": "Subham",
                "acc_det": 2000
            }},
            { "_id": 3,
            "name": "Jeeshan", 
            "password": 1234,
            "balance": 100000,
            "addPayee": {
                "name": "Hagi",
                "acc_det": 2000
            }}
    ]
    x = mycol.insert_many(dataBase)
    print(x.inserted_ids)