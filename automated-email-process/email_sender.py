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
body_text = "Hi, \n I am an automated email, How's you \n Thanks \n Json Macciller"
subject_text = "Automated Email Test"

"""Automated Email Process function Args:"""
def send_mail(send_from, send_to, subject, message, files=["/Users/aashishsaini/PycharmProjects/amazon-scraper/8875140406112019.pdf"],
              server="smtp.gmail.com", port=587, username="bestviewsreviews@gmail.com", password='Best@xy123',
              use_tls=True):#Replace the path of files variable in case of change the path of the file
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

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

"""calling a function"""
for i in email_list:
    try:
        send_mail(send_to=email_list[a], send_from="Json_macciller@apple.com",subject=subject_text,message=body_text)
        print(Fore.LIGHTGREEN_EX+"email has been successfully sent to -> "+email_list[a])
    except:
        cprint("email has not been successfully sent to -> " + email_list[a], 'red', attrs=['blink'])
    a = a+1
