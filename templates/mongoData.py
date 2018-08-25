import pymongo,pprint,json,time
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["Customers"]
dataBase={
        "_id": 1,
        "name": "Sankho", 
        "password": '1234',
        "balance": 22222222,
        "addPayee": {
            "Added_User_Name": ["Podu","Baban"],
            "acc_det": [2000000,400000000]
        }
}
time.sleep(3)
posts= mydb.posts
#post_id= posts.insert_one(dataBase).inserted_id
#Above line is used to insert into Collection
updatedVal = posts.find_one()
json_str= json.dumps(updatedVal)#converting dict to a str obj
resp = json.loads(json_str)