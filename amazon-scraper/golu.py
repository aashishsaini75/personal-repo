import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from email_list import email_list
from colorama import Fore, Back, Style
from termcolor import colored, cprint

"""Loop Counter"""
a= 0

"""Email data"""
body_text = "Dear candidate, \n We are pleased to inform you that you are selected for our respected organizations.\n your profile has been shortlisted by our Recruiting board member for further details and process do read the letter and confirm your attendance by following rules and regulations,\n Regards \n Recruiting Team"
subject_text = "[Interview Letter]"

"""Automated Email Process function Args:"""
def send_mail(send_from, send_to, subject, message, files=['/Users/aashishsaini/PycharmProjects/amazon-scraper/Document4.pdf'],
              server="relay-hosting.secureserver.net", port=465, username="Career@tcs-supports.co.in", password='123456',
              use_tls=True):
    #Replace the path of files variable in case of change the path of the file

    """Compose and send email with provided info and attachments.
    Args:
        send_from (str): from name
        send_to (str): to name
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    """Loop to attach a files"""
    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(op.basename(path)))
        msg.attach(part)

    smtp = smtplib.SMTP_SSL(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

"""calling a function"""
for i in email_list:
    # try:
        send_mail(send_to=email_list[a], send_from="Career@tcs-supports.co.in",subject=subject_text,message=body_text)
        print(Fore.LIGHTGREEN_EX+"email has been successfully sent to -> "+email_list[a])
        print("Total email sent "+ str(a))
    # except:
        cprint("email has not been successfully sent to -> " + email_list[a], 'red', attrs=['blink'])
    # a = a+1
