import pandas as pd
import datetime
import smtplib
import os
GMAIL_ID=''
GMAIL_PSWD=''
def sendEmail(to,sub,msg):
    print(f"email to{to} subject{sub}message{msg}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"{sub}\n\n{msg}")
    s.quit()
    pass
if __name__== "__main__":
    sendEmail(GMAIL_ID,"subject","test")
    df=pd.read_excel("birth.xlsx")
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    writeInd=[]
    for index,item in df.iterrows():
        bday=item['Birthday'].strfirm("%d-%m")
        msg="happy birtday.ur sweetest person i have met"
        if(today==bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'],"happy birthday",item['Dialogue'])
            writeInd.append(index)
for i in writeInd:
    yr=df.loc[i,'Year'] =str(yr)+','+str(yearNow)

    df.to_excel("birth.xlsx",index=False)


