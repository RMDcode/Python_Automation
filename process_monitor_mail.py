import os
import time
import psutil
import smtplib
import schedule
import urllib.request
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        print("Unable to establish a connection to the URL:", err)
        return False

    

    if is_connected('http://www.google.com'):
        print("Internet connection established to", url_to_check)
    else:
        print("No internet connection to", url_to_check)



#def is_connected():
#    try:
#        urllib.request.urlopen('http://216.58.192.142', timeout=1)
#        return True
#    except urllib.request.URLError as err:
#        return False

def MailSender(filename, time):
    try:
        fromaddr = "dhurir163@gmail.com"
        toaddr = "dhurirohit4@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystems.
        Please find attached document which contains the log of Running processes.
        Log File is created at: %s

        This is an auto-generated mail.

        Thank & Regards,
        Piyush Manohar Khairnar
        Marvellous Infosystems
        """ % (toaddr, time)

        Subject = """
        Marvellous Infosystems Process log generated at: %s
        """ % (time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename=%s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(fromaddr, "wevf wmal brce nsja")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log File successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail", E)

def ProcessLog(log_dir = 'C:\\Users\\Lenovo\\Desktop\\Python\\Automation\\MarvellousLog'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    log_path = os.path.join(log_dir, f"MarvellousLog_{timestamp}.log")

    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger: " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % log_path)

    if is_connected():
        startTime = time.time()
        MailSender(log_path, time.ctime())
        endTime = time.time()

        print("Took %s seconds to send mail" % (endTime - startTime))
    else:
        print("There is no internet connection")

def main():
    print("------Marvellous Infosystems------")

    print("Application name:", argv[0])

    if (len(argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to log records of running processes")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError as v:
        print("Error: Invalid datatype of input",v)

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
