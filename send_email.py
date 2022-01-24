from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="datacollectorapp1@gmail.com"
    from_password="udemylecture"
    to_email=email #user input to func call to email
    subject="Height Data"

    #html enabled thru mimetext; height in bold; string text used
    message="Hi, your height is <strong>%s</strong>. The average height of all entries is <strong>%s</strong> out of <strong>%s</strong> people." % (height, average_height, count)
    msg=MIMEText(message, 'html') #allows 'message' read as html
    #access keys from msg obj to set values
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    #log into from email
    gmail=smtplib.SMTP('smtp.gmail.com',587) #server address and port
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password) #gets credentials
    #sendmessage method on gmail obj and pass message='msg'
    gmail.send_message(msg)
