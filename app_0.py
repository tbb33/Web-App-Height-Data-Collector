from flask import Flask, render_template, request

app=Flask(__name__) #var to store flask obj instance/app

@app.route('/') #home pg
def index():
    return render_template("index.html") #renders index.html in home pg

@app.route('/success', methods=['POST']) #after press button
def success():
    if request.method=='POST':
        #get email/ht from http request
        email=request.form["email_name"] #form tag; stores input into email var
        height=request.form["height_name"]
        print(request.form)
        print(email,height)
        return render_template("success.html")

#means if scripts being executed and not imported then execute lines below
if __name__=="__main__":
    app.debug=True
    app.run()
