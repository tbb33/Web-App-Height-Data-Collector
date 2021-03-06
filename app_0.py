from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__) #var to store flask obj instance/app
#conn db
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:eclerx#123@localhost/height_collector_0'
db=SQLAlchemy(app) #creating sqlalchemy obj for flask app 'app'

class Data(db.Model):
    __tablename__='data' #creates tbl
    #creating cols; all vars local vars to ea func
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)
    #initialize instance vars
    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route('/') #home pg
def index():
    return render_template("index.html") #renders index.html in home pg

@app.route('/success', methods=['POST']) #after press button
def success():
    if request.method=='POST':
        #get email/ht from http request
        email=request.form["email_name"] #form tag; stores input into email var
        height=request.form["height_name"]

        #filter data where email=user email
        if db.session.query(Data).filter(Data.email_==email).count() ==0:
            data=Data(email,height)
            #Data class create db model obj which recognized by add method of sqlalchemy obj
            db.session.add(data) #add rows
            db.session.commit() #commit changes
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
        else:
            return render_template("index.html",
            text="We have already received a submission from that email address. Please submit a new email address to continue.")

#means if scripts being executed and not imported then execute lines below
if __name__=="__main__":
    app.debug=True
    app.run()
