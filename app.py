from flask import Flask, render_template, request, redirect, url_for, session, flash
from wtforms import Form, form, StringField, TextAreaField, RadioField, SelectField, validators, PasswordField,SelectField,IntegerField
from wtforms.fields.html5 import EmailField
from datetime import datetime, date


import shelve
import Account
import User
import os
import Transactions

app = Flask(__name__)
app.secret_key = os.urandom(24)

class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)


import Form
from Form import Feedback

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    form = Feedback()
    userList = {}
    messagelist = {}
    db = shelve.open('storage.db')
    messagelist = db['messagelist']

    userList = db['Users']
    id = session['id']
    if form.validate_on_submit():

        user = userList.get(id)
        feedback = {'user': session.get('firstname'),
                    'subject': form.subject.data,
                    "feedback": form.content.data,
                    'time': str(datetime.now().strftime('%B %d %H:%M'))}

        print(feedback['time'])
        messagelist.append(feedback)
        print(messagelist)
        db['messagelist'] = messagelist
        db.close()
        # return redirect(url_for('index'))
        # db.close()
    return render_template("feedback.html", form=form, messagelist=messagelist)

#jerome's part (i added it in)
@app.route('/topup', methods=['GET', 'POST'])
def topup():

    form = Form.TopUp(request.form)
    print("topup")
    userList = {}
    db = shelve.open('storage.db', 'w')
    userList = db['Users']
    id = session['id']
    if request.method == 'POST' and form.validate():

        user = userList.get(id)
        balance = form.balance.data + user.get_balance()
        user.set_balance(balance)

        db['Users'] = userList
        session['balance'] = user.get_balance()
        db.close()
        return redirect(url_for('index'))
        db.close()

    else:
        print("fail")
        db.close()

    return render_template('added/topup.html',form=form)



@app.route('/index')
def index():

    return render_template('added/index.html')

@app.route('/', methods=['GET','POST'])
def login():
    form = Form.UserLogin(request.form)
    if request.method == 'POST' and form.validate():
        userList = {}
        db = shelve.open('storage.db', 'r')
        print("db open")
        userList = db['Users']
        list = []

        for key in userList:
            user = userList.get(key)
            list.append(user)

            if (user.get_email() == form.email.data) and (user.get_password() == form.password.data):
                session['firstname'] = user.get_firstname()
                session['lastname'] = user.get_lastname()
                session['balance'] = user.get_balance()
                session['id'] = user.get_userID()
                session['email'] = user.get_email()
                session['phonenumber'] = user.get_phonenumber()
                session['password'] = user.get_password()
                session['accountnumber']= user.get_accountnumber()
                print(session['id'])

                return redirect(url_for('index'))
                print("success")
                db.close()

            else:
                print("fail")
                db.close()

    return render_template('added/login.html', form=form)

#remove balance cuz we wont let them register balance anymore
@app.route('/register', methods=['GET', 'POST'])
def newUser():
    form = Form.RegisterUser(request.form)
    if request.method == 'POST' :

        userList = {}
        db = shelve.open('storage.db', 'c')

        try:
            userList = db['Users']
        except:
            print("fail in open db")

        #userid = len(userList) + 1
        user = User.User(form.firstname.data, form.lastname.data, form.email.data, form.phonenumber.data, form.password.data,form.accountnumber.data)

        userList[user.get_userID()] = user
        db['Users'] = userList

        db.close()

        return redirect(url_for('login'))

    return render_template('added/register.html', form=form)

@app.route('/forgot-password')
def password():
    return render_template('forgot-password.html')


@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/createTransactionsDB', methods=['GET', 'POST'])
def createTransactionsDB():
    db = shelve.open('storage.db', writeback = True)
    transactionsList = []
    db['Transactions'] = transactionsList
    db.close()

    return 'Transactions Object Created'

@app.route('/appendDB')
def appendDB():

    accountList = []

    try:
        db = shelve.open('storage.db', writeback=True)
        import_file = open('appendData.txt', 'r')
        accountList = db['Account']

        for accountInfo in import_file:
            list = accountInfo.split(',')
            account = Account.Account(str(list[0]), str(list[1]), float(list[2]), str(list[3]))
            accountList.append(account)

    except:
        print("fail in open db")

    db['Account'] = accountList
    db.close()

    return 'Database Updated'

@app.route('/dumpDB')
def dumpDB():
    db = shelve.open('storage.db', 'r')
    myfile = open('dumpData.txt', 'w')
    userList = db['Account']
    db.close()
    list = []
    for key in userList:
        # user = userList[key]
        # list.append(user)
        list.append(key)

        tmpString = str(key.get_AccountNo())
        myfile.write(tmpString)
        myfile.write(", ")
        myfile.write(key.get_Type())
        myfile.write(", ")
        myfile.write(str(key.get_Balance()))
        myfile.write(", ")
        myfile.write(key.get_userID())
        myfile.write("\n")

    myfile.close()
    return "data dumped"


@app.route('/formsuccess', methods=['GET', 'POST'])
def formsuccess():

    if request.method=="POST":
        sender=request.form['Sender']
        receiver=request.form['Receiver']
        bank=request.form['Bank']
        type=request.form['Type']
        amount=request.form['Amount']
        accountno=request.form['AccountNo']
        time=request.form['Time']

        db =shelve.open('storage.db',writeback=True)
        transferList=db['Account']





    return render_template('added/formsuccess.html', sender=sender, receiver=receiver,bank=bank,type=type,amount=amount,accountno=accountno,time=time)

   #if request.method == "POST":

        # Step 2 : assign variables to the values obtained from HTML form
        #name = request.form['Name']
        #email = request.form['Email']
        #bank = request.form['Bank']


        # Step 3: check bank balance and stuff

        #db = shelve.open('storage.db', writeback=True)
        #userList = db['Users']
        #for userID in userList:

            #userList[userID].set_balance(balance)
    #    db['Account']=transferList
    #    user=userList
    #
    #    if form.Amount.data <= user.get_balance():
    #
    #
    #        balance=user.get_balance()-form.Amount.data
    #        user.set_balance(balance)
    #        db['User']=userList
    #        session['balance']=user.get_balance()


    #return render_template('added/formsuccess.html', name=name, email=email, bank=bank)


#renae's part(to get out the form)

@app.route('/blank', methods=['GET', 'POST'])
def blank():
    if request.method == 'GET':

        db = shelve.open('storage.db', 'r')
        transactionsList = db['Transactions']
        for transaction in transactionsList:
            print(transaction)

        inwardList = []
        print('session[firstname] is: {}'.format(session['firstname']))

        for transactionObject in transactionsList:
            if transactionObject.get_receiver() == session['firstname']:
                inwardList.append(transactionObject)

        db.close()

        # return template for GET method
        return render_template('blank.html', inwardList=inwardList)

@app.route('/transfer', methods=['GET','POST'])
def transfer():

    return render_template('added/ftransfer.html')



@app.route('/final', methods=["POST"])
def final():

    # usage of python codes for html form

    if request.method == "POST":
        sender = request.form['Sender']
        receiver = request.form['Receiver']
        amount = request.form['Amount']
        userid = request.form['UserID']



        db = shelve.open('storage.db', writeback=True)
        userList = db['Users']
        transferList=db['Account']

        """
                Clement's part here.

                Create objects of transactions, then append to list

                Assign this list to db['Transactions]
                """
        transactionList = db['Transactions']

        today = datetime.today().date()

        newTransaction = Transactions.Transactions(amount, today, sender, receiver)

        transactionList.append(newTransaction)
        # Logic to deduct amount from account's balance

        for index in userList:
            if index == session['id']:
                currentBalance = userList[index].get_balance()

        #I changed this :to check if the user input matches a key in the database (to check if it matches any of the other users in db)
        for userid in userList:
            payee= userList.get(userid)


        #changed this too
        if float(amount)<= float(currentBalance):
            newBalance  = float(currentBalance) - float(amount)
            newPayeeBalance= float(amount) + float(payee.get_balance())

            for index in userList:
                if index == session['id']:
                    userList[index].set_balance(newBalance)

            for userid in userList:
                userList[userid].set_balance(newPayeeBalance)

        db['Transactions']=transactionList
        db['Users'] = userList
        db.close()


    return render_template('added/final.html', sender=sender, receiver=receiver,amount=amount, userid=userid, newBalance=newBalance,newPayeeBalance=newPayeeBalance)



@app.route('/Transaction')

def transaction():
    return render_template('Transaction.html')


@app.route('/Limits')
def limits():
    return render_template('Limits.html')

@app.route('/logout')
def logout():
    db=shelve.open('storage.db','c')
    if session.get('firstname'):
        session.pop('firstname')
    if session.get('lastname'):
        session.pop('lastname')
    if session.get('email'):
        session.pop('email')
    if session.get('balance'):
        session.pop('balance')
    if session.get('phonenumber'):
        session.pop('phonenumber')
    if session.get('balance'):
        session.pop('balance')
    if session.get('id'):
        session.pop('id')
    db.close()
    print('db closed')
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
