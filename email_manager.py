import os
from smtplib import SMTP


class EmailManager():

    HOST = 'smtp.gmail.com'
    PORT = 587
    SENDER_EMAIL = 'mohamedzaki02@gmail.com'
    USERNAME = os.environ.get('MY_EMAIL')
    PASSWORD = os.environ.get('MY_PASSWORD')

    def __init__(self):
        pass

    def send_email(self, subject, body, receiver_email):
        with SMTP(host=self.HOST, port=self.PORT) as connection:
            connection.starttls()
            connection.login(self.USERNAME, self.PASSWORD)
            connection.sendmail(
                from_addr=self.SENDER_EMAIL, to_addrs=receiver_email, msg=f"Subject:{subject}\n\n{body}")
