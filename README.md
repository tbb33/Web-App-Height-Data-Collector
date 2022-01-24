# Web-App-Height-Data-Collector

## This web app, built using python and Flask, will store users' data in PostgreSQL database, make some calculations, and send results to user's email address.
#### I've deployed my app online. Have a look: http://taylorhfam.pythonanywhere.com/
#### To execute this app locally, run app_0.py and open browser to http://localhost:5000/ (or wherever your terminal specifies) but please look at the notes section to ensure the app will run properly.

<br>

The frontend of my web app uses CSS and HTML, and the backend uses python.

<br>

Description of folders/files:
1. app_0.py - backend code, connects to database, performs calculations
2. send_email.py - contains send_email function that sends email to user containing data and calculations
3. templates folder - HTML files
   - index.html - html code for home page
   - success.html - html code for success page (after click submit button on home page)
4. static folder - CSS 
   - main_0.css - stylizes html code/web pages
<br>

<br>

Notes to run the above files, you need:
1. postgresql db server installed on your computer (I used pgadmin) and then create a database (mine is height_collector_0) and then change the information respectively (db name and password) in the following line in app_0.py:
   - app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:eclerx#123@localhost/height_collector_0'
2. install psychopg2, install Flask-SQLAlchemy
3. create the table
   - In cmd in VE type‘python’ ‘from app_0 import db’ then ‘db.create_all()’
4. if you change the from_email in the send_email funciton to your own email, change the password too and if it's a gmail account:
   - google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure", so what you have to do is go to this link while you're logged in to your google account, and allow the access:
https://www.google.com/settings/security/lesssecureapps!
5. ensure all files/folders are in the same directory. 




