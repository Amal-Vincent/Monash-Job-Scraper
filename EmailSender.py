import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from baselogging import *

class email_sender():
    
    def __init__(self):
        self.mail = smtplib.SMTP('smtp.gmail.com',587)
        self.email_sender = 'Provide from email here'
        self.email_receiver = 'provide to email here'
        self.email_password  = 'From email password' 
        
    def send_email(self,content_list,email_subject):
        msg = MIMEMultipart()
        msg['From'] = self.email_sender
        msg['To'] = self.email_receiver
        msg['Subject'] = email_subject
        body = ""
        for dic in content_list:
            for key,value in dic.items():
                body = body + " \n" + key + " : " + value
            body = body + "\n"
        log.info("email body " + " \n" + str(body))
        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
        self.mail.ehlo()
        self.mail.starttls()
        log.info("connected to gmail")
        self.mail.login(self.email_sender,self.email_password)
        self.mail.sendmail(self.email_sender,self.email_receiver,text)
        log.info("email send")
        
        
def main():
    email = email_sender()
    
    
if __name__ == "__main__":
    main()