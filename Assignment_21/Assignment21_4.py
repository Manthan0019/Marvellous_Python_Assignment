import os
import sys 
import psutil
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

def ProcInfo():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace("/","_")
    timestamp = timestamp.replace(":","_")

    filename = os.path.join(FolderName,"ProcessInfo%slog.log"%(timestamp))
    
    fobj = open(filename,"w")

    Border = ("-")*80
    fobj.write(Border)
    fobj.write("\n\t\tTihs is a cureent running process log file \n")
    fobj.write("\t\tThis log file is created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    Data = ProcInfo()

    for value in Data:
        fobj.write("%s \n\n"%(value))
    
    fobj.write(Border)

    fobj.close()

    return filename

def SendMail(FolderName, ReceiverMail, SenderMail, SenderPassword):
    filename = CreateLog(FolderName)

    msg = MIMEMultipart()
    msg['From'] = SenderMail
    msg['To'] = ReceiverMail
    msg['Subject'] = "Process Log File Generated"

    body = "Please find attached the log file containing current running processes information."
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SenderMail, SenderPassword)
        text = msg.as_string()
        server.sendmail(SenderMail, ReceiverMail, text)
        server.quit()
        print("Log file sent successfully to %s"%(ReceiverMail))
    except Exception as e:
        print("Unable to send email : ",e)
def main():
    if(len(sys.argv)== 2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This is the automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail.")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use this script as ScriptName.py DirectoryName TimeInterval")
    elif(len(sys.argv)==4):
        DirectoryName = sys.argv[1]
        ReceiverMail = sys.argv[2]
        TimeInterval = int(sys.argv[3])

        print("Enter sender's email ID:")
        SenderMail = input()

        print("Enter sender's email password:")
        SenderPassword = input()

        schedule.every(TimeInterval).minutes.do(SendMail, DirectoryName, ReceiverMail, SenderMail, SenderPassword)

        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("please use --h for help and --u for usage")
        print("Please enter valid inputs")
if __name__ == "__main__":
    main()