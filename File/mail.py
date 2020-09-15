# import smtplib

#   server = smtplib.SMTP("smtp.gmail.com",587)
#   server.login("sherlock.holmes8907891","sherlock@123")
#  smtplib.SMTP.login("sherlock.holmes8907891","sherlock@123")
#  smtplib.SMTP.starttls()
# server.starttls()
#  smtplib.SMTP.sendmail("sherlock.holmes8907891","ssankethboss061@gmail.com","hello")
#  smtplib.SMTP.quit()

import smtplib, ssl

with open("credentials.txt") as f:
    user_name=f.readline().strip()#remove strailing spaces from string
    password=f.readline()
    
    
def mail(to,sub,msg):
    
    mail_dict={
        "sanketh":"ssankethboss061@gmail.com",
        "elon":"sankeths94@gmail.com"
    }
    rec=mail_dict.get(to)
    # print(to)
    # print(sub)
    # print(msg)
    # print(user_name)
    # print(len(user_name))
    # user_name = "sherlock.holmes8907891"
    
    # print(len(user_name))
    # print(len(password))
   
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    
    

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(user_name, password)
        # TODO: Send email here
        server.sendmail(user_name,rec,f"Subject: {sub}\n\n {msg}")
        print(f"mail sent to {to} sucessfully! ")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


mail("sanketh","testsub","test message") 
    
print(user_name)
print(password)