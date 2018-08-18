from flask import *
from templates import account
SECRET_KEY = "sankhojjal"
app = Flask(__name__)
app.config.from_object(__name__)
accObj=account.Account('Sankho',12345,1000000)
FLAG = False
'''@app.route("/")
def home(name= None):
    return render_template("index.html", name= name)'''

@app.route("/", methods = ["GET", "POST"])
def login():
    error= None
    if request.method == 'POST':
        if request.form['username']== "sankho" and request.form["password"] == "1234":
           #session["logged_in"]= True 
            global FLAG 
            FLAG=True
            return redirect(url_for("dashBoard"))
        else:
            error = "User or passowrd wrong"
    return render_template("login.html", error= error)

@app.route("/dashBoard")
def dashBoard():
    if(FLAG== True):
        return render_template("dashBoard.html")
    else:   
        return redirect(url_for("login"))

@app.route("/addPayee.html", methods=['GET','POST'])
def addPayee():
    if(FLAG== True):
        if request.method == 'GET':
            return render_template("addPayee.html")
        else:
            name= request.form['name']
            acc_Num= request.form['acc_num']      
            accObj.addPayeeDetails(acc_Num,name)
            return render_template("dashBoard.html")
    else:
         return redirect(url_for("login"))

@app.route("/removePayee.html",methods=['GET','POST'])
def removePayee():
    if(FLAG== True):
        if request.method == 'GET':
            return render_template("removePayee.html")
        else:
            acc_Num= request.form['acc_num']
            accObj.removePayeeDetails(acc_Num)
            return render_template("dashBoard.html")
    else:
         return redirect(url_for("login"))

@app.route("/moneyTransfer.html")
def transferMoney():
    if(FLAG== True):
        return render_template("transferMoney.html")
    else:
         return redirect(url_for("login"))

@app.route("/depositMoney.html")
def depositMoney():
    if(FLAG== True):
        return render_template("depositMoney.html")
    else:
         return redirect(url_for("login"))

app.run(debug=True)