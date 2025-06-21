import os 
import time
import sys
import hashlib
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
def CreateLog():
    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace("/","_")
    timestamp = timestamp.replace(":","_")

    filename = "Deletion%slog.log"%(timestamp)
    
    fobj = open(filename,"w")

    Border = ("-")*80
    fobj.write(Border)
    fobj.write("\n\t\tTihs is a log file which contins deleted file names \n")
    fobj.write("\t\tThis log file is created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.close()

    return filename

def GetChecksum(path,Blocksize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(Blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(Blocksize)
    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("No such directory")
        exit()

    flag = os.path.isdir(DirectoryName)
    
    if(flag == False):
        print("Pathe is valid but targate is not a directory")
        exit()

    Duplicate = {}

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = GetChecksum(fname)
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

def DeleteDuplicate(ReceiverMail, SenderMail, SenderPassword,Path = "Marvellous"):
    fileName=CreateLog()
    fobj = open(fileName,"a")

    StartTime = time.ctime()

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda X : len(X) > 1, MyDict.values()))

    TotalFiles = sum([len(files) for files in MyDict.values()])
    TotalDuplicate = sum([len(files)-1 for files in Result])

    count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            count = count + 1
            if(count > 1):
                fobj.write("Deleted file name :"+subvalue+"\n\n")
                os.remove(subvalue)
                cnt = cnt + 1
        count = 0

    
    fobj.write("Total duplicate files deleted : "+str(cnt)+"\n")
    
    SendMail(ReceiverMail, SenderMail, SenderPassword,fileName,StartTime,TotalFiles,TotalDuplicate)

def SendMail(ReceiverMail, SenderMail, SenderPassword,filename,StartTime,TotalFiles,TotalDuplicate):

    msg = MIMEMultipart()
    msg['From'] = SenderMail
    msg['To'] = ReceiverMail
    msg['Subject'] = "Deletion Log File Generated"

    body = ("Scanning started at : "+StartTime+"\n"+
        "Total files scanned : "+str(TotalFiles)+"\n"+
        "Total Duplicate files : "+str(TotalDuplicate)+"\n"
        "Scan ended at : "+time.ctime()+"\n")
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