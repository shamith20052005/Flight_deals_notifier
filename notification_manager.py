import smtplib
import os
import requests
from dotenv import load_dotenv
# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.my_email = os.getenv("MY_EMAIL")
        self.my_password = os.getenv("MY_EMAIL_PASSWORD")
        self.smtp_address = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")

    def send_emails(self, email_list, email_body):
        try:
            with smtplib.SMTP(self.smtp_address, timeout=30) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.my_password)
                for email in email_list:
                    connection.sendmail(
                        from_addr=self.my_email,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                    )
            print("Emails sent successfully!")
        except (smtplib.SMTPException, TimeoutError) as e:
            print(f"Failed to send emails: {str(e)}")

    def telegram_bot_send_text(self, bot_message):
        bot_token = os.environ["BOT_TOKEN"]
        bot_chatID = os.environ["BOT_CHATID"]
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
                    + '&parse_mode=Markdown&text=' + bot_message
        bot_response = requests.get(send_text)
        return bot_response.json()
