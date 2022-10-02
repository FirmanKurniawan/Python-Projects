import smtplib

#Before executing, go to-
#gmail->account->security->less secure apps->turn on access

print("----- Email sender -----")
#sender mail
sender_mail = input("- Enter your mail --> ")
#receiver mail
receiver_mail = input("- Enter receiver's mail --> ")
#message
message = """From : From mail
To : To mail
Subject : test mail
If you dont use gmail, u boomer.
"""%(sender_mail,receiver_mail)
try:
    #password
    password = input("- Enter your password --> ")
    smtpobj = smtplib.SMTP("smtp.gmail.com",587)
    smtpobj.login(sender_mail,password)
    smtpobj.sendmail(sender_mail,receiver_mail,message)
    #positive case
    print("- Successfully sent email.")
except Exception:
    #negative case
    print("- Unable to send email!")
