import os
import time
import psutil
import smtplib
import schedule
import urllib.request
from sys import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        print("Unable to establish a connection to the URL:", err)
        return False

def MailSender(time):
    try:
        fromaddr = "dhurir163@gmail.com"
        toaddr = "dhurirohit4@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        subject = "Marvellous Event Hub"
        msg['Subject'] = subject

        body = """
        Dear sir/madam,

        Good Day!

        We are thrilled to confirm your registration for the upcoming Online Event. Thank you for choosing to be a part of this exciting event. We look forward to your participation. Here are the details of your registration:

        Don't miss out on:
        - Engaging sessions with industry experts
        - Opportunities to network with fellow participants
        - Q&A sessions to get your questions answered

        To join the event, we will share a Zoom link before the scheduled time.

        If you haven't registered yet, there's still time! Register now to secure your spot.

        We understand that life can get busy, but we encourage you to set a reminder and join us for this insightful event. We value your presence and insights.

        If you have any questions or need assistance, please don't hesitate to reach out to our support team at dhurir163@gmail.com or +91 9552248843.

        Stay Tuned with below contents for your reference:
        https://youtu.be/l1CGQqOxcvY?si=Knw8Hh5vJ9tTAue4

        Thank you for your interest.

        Best regards,

        Rohit Manoj Dhuri
        Head Organizer
        Marvellous Event Hub

        P.S. Stay connected with us on social media: https://www.linkedin.com/in/rohit-dhuri-2b8848190.
        """

        msg.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "wevf wmal brce nsja")

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        print("Email sent successfully")

    except Exception as E:
        print("Unable to send email", E)

def main():
    print("------Marvellous Infosystems------")
    print("Application name:", argv[0])

    try:
        if is_connected():
            startTime = time.time()
            MailSender(time.ctime())
            endTime = time.time()
            print("Took %s seconds to send email" % (endTime - startTime))
        else:
            print("There is no internet connection")

    except ValueError as v:
        print("Error: Invalid datatype of input", v)

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
