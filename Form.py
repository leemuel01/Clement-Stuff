#renae's part
from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import Form, form, StringField, TextAreaField, RadioField, SelectField, validators, PasswordField, \
    SelectField, IntegerField, SubmitField
from wtforms.fields.html5 import EmailField
from datetime import datetime, date

from wtforms.validators import DataRequired, Length


class FundTransfer(Form):
    Sender = StringField('Sender', [validators.Length(min=1, max=100), validators.DataRequired()])
    Receiver = StringField('Receiver', [validators.Length(min=1, max=100), validators.DataRequired()])
    Bank = SelectField('Bank', choices=[('DBS/POSB'), ('OCBC'), ('UOB'),('HSBC'),('Maybank'),('Bank of China'),('Standard Chartered')], default='DBS/POSB')
    Type=SelectField('Type', choices=[('Deposit'),('Loan'),('Current')],default='Deposit')
    Amount = IntegerField('Amount', [validators.Length(min=1, max=100), validators.DataRequired()])
    AccountNo = IntegerField('AccountNo', [validators.Length(min=1, max=8), validators.DataRequired()] )
    Time = SelectField('Time', choices=[('Immediate'),('Future')], default='Immediate')
    Balance=StringField('Balance' , [validators.Length(min=1 , max=10000), validators.DataRequired()])\

#jerome's part

from flask import Flask, render_template, request, redirect, url_for, session
from wtforms import Form, form, StringField, TextAreaField, RadioField, SelectField, validators, PasswordField, \
    SelectField, IntegerField, StringField, StringField, StringField
from wtforms.fields.html5 import EmailField
from datetime import datetime, date

class RegisterUser(Form):
    firstname = StringField('firstname', [validators.Length(min=1, max=150), validators.DataRequired()])
    lastname = StringField('lastname', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = PasswordField('password', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('email', [validators.DataRequired(), validators.Email()])
    phonenumber=StringField('phonenumber',[validators.length(min=8,max=20),validators.data_required])
    accountnumber = IntegerField('Account Number', [validators.length(min=1, max=20), validators.DataRequired()])
    balance = 0

#jerome's part

class UserLogin(Form):
    email = EmailField('email', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])

#jerome's part
class TopUp(Form):
    cardnumber= IntegerField('card number', [validators.DataRequired()])
    balance = IntegerField('balance', [validators.DataRequired()])
    accountnumber=  IntegerField('Account number', [validators.DataRequired()])

class Feedback(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])

    content = TextAreaField("Content", validators=[DataRequired(),Length(max=255)])

    submit = SubmitField("Submit")