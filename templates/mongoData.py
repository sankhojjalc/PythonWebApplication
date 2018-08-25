import pymongo,pprint,json,time
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["Customers"]
dataBase={
        "_id": 1,
        "name": "Sankho", 
        "password": '1234',
        "balance": 22222222,
        "addPayee": [{
            "name": "Podu",
            "acc_det": 2000
        },
        {
            "name": "Prateek",
            "acc_det": 2000
        }]
} 
# mycol.update(
#     {"name": 'Sankho'},
#     {"$set":{"balance": 66666666},
#     },
#     upsert=False
#     )
time.sleep(3)
posts= mydb.posts
#post_id= posts.insert_one(dataBase).inserted_id
#Above line is used to insert into Collection
#pprint.pprint(posts.find_one())
updatedVal = posts.find_one()
json_str= json.dumps(updatedVal)#converting dict to a str obj
resp = json.loads(json_str)
#print(resp["name"])
print(resp["balance"])