from flask import *
from templates import account, mongoData
SECRET_KEY = "sankhojjal"
app = Flask(__name__)
app.config.from_object(__name__)
accObj=account.Account()
FLAG = False
@app.route("/", methods = ["GET", "POST"])
def login():
    error= None
    if request.method == 'POST':
        if request.form['username']== mongoData.resp['name'] and request.form["password"] == str(mongoData.resp['password']):
            global FLAG 
            FLAG=True
            return redirect(url_for("dashBoard"))
        else:
            error = "User or passowrd wrong"
    return render_template("login.html", error= error)

@app.route("/dashBoard")
def dashBoard():
    UserName= mongoData.resp['name']
    balance = mongoData.resp['balance']
    
    if(FLAG== True):
        return render_template("dashBoard.html",UserName=UserName,balance=balance)
    else:   
        return redirect(url_for("login"))

@app.route("/addPayee.html", methods=['GET','POST'])
def addPayee():
    UserName= mongoData.resp['name']
    balance = mongoData.resp['balance']
    if(FLAG== True):
        if request.method == 'GET':
            return render_template("addPayee.html")
        else:
            name= request.form['name']
            acc_Num= request.form['acc_num']      
            accObj.addPayeeDetails(acc_Num,name)
            return render_template("dashBoard.html",UserName=UserName,balance=balance)
    else:
         return redirect(url_for("login"))

@app.route("/removePayee.html",methods=['GET','POST'])
def removePayee():
    UserName= mongoData.resp['name']
    balance = mongoData.resp['balance']
    if(FLAG== True):
        if request.method == 'GET':
            return render_template("removePayee.html")
        else:
            name= request.form['name']
            acc_Num= request.form['acc_num']
            accObj.removePayeeDetails(name,acc_Num)
            return render_template("dashBoard.html",UserName=UserName,balance=balance)
    else:
         return redirect(url_for("login"))

@app.route("/moneyTransfer.html",methods=['GET','POST'])
def transferMoney():
    if(FLAG== True):
        if request.method=='GET':
            return render_template("transferMoney.html")
        else:
            amount = int(request.form['amount'])
            balance = mongoData.resp['balance']
            dummyVar= accObj.transferMoney(amount,balance)
            if(dummyVar== False):
                error= "Not Sufficient message"
                return render_template("transferMoney.html", error= error)
            else:
                UserName= mongoData.resp['name']
                UpdatedBalance = mongoData.resp['balance']
                return render_template("dashBoard.html",UserName=UserName,balance=UpdatedBalance)
    else:
         return redirect(url_for("login"))

@app.route("/depositMoney.html",methods=['GET','POST'])
def depositMoney():
    if(FLAG== True):
        if request.method=='GET':
            return render_template("depositMoney.html")
        else:
            amount = int(request.form['amount'])
            balance = mongoData.resp['balance']
            accObj.depositMoney(amount,balance)
            UserName= mongoData.resp['name']
            UpdatedBalance = mongoData.resp['balance']
            return render_template("dashBoard.html",UserName=UserName,balance=UpdatedBalance)
    else:
         return redirect(url_for("login"))


app.run(debug=True)