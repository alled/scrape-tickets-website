import smtplib
import os
from dotenv import load_dotenv

carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@page.nextel.com',
    'telus': '@msg.telus.com'
}


def send(message):

    # load env variables from .env environment file
    load_dotenv()

    to_number = os.environ.get('PHONE_NUMBER_TO_SEND_NOTIFICATION_TO')+'{}'.format(carriers['telus'])
    auth = (os.environ.get('GMAIL_EMAIL'), os.environ.get('GMAIL_PASSWORD'))

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)
    print('sms has been sent '+message)
