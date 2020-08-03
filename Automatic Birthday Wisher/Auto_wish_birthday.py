import pandas
import datetime
import smtplib,ssl

with open("credentials.txt") as f:
    user_name=f.readline().strip()#remove strailing spaces from string
    password=f.readline()

def mail(to,sub,msg):
    
    # mail_dict={
    #     "sanketh":"ssankethboss061@gmail.com",
    #     "elon":"sankeths94@gmail.com"
    # }
    # rec=mail_dict.get(to)
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
        server.sendmail(user_name,to,f"Subject: {sub}\n\n {msg}")
        print(f"mail sent to {to} sucessfully! ")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

df=pandas.read_excel("Data.xlsx")
print(df)# 2d array

print(type(df))

print(len(df))
today=datetime.datetime.now().strftime("%m-%d")
print(today)
marking_wished=[]
year=datetime.datetime.now().strftime("%Y")

# print(df.index)#returns a range
for i in df.index:
    # print(df['Email'][i],df['name'][i])
    bday=df['Date'][i].strftime("%m-%d")
    print(df['Date'][i].strftime("%m-%d"))
    if today==bday and year not in str(df.loc[i,'Year']):
        print(f" Wishing   {df['name'][i]}")
        marking_wished.append(i)
        to=str(df.loc[i,'Email'])
        msg=str(df.loc[i,'Dialogue'])
        mail(to,"Happy birthday",msg)
    # print(df['sl no'][i])
    # print(df['name'][i])

# print(marking_wished)
# print(type(marking_wished[0]))

for i in marking_wished:
    print(df.loc[i,'Year'])
    print(type(df.loc[i,'Year']))
    print(year)
    df.loc[i,'Year']=str(df.loc[i,'Year'])+","+str(year)
    # df.loc[i,'name']="Elon Musk1"
    
print(df.loc[2,'Year'])
df.to_excel('Data.xlsx',index=False)# dont write any unamed index to data.xlsx
