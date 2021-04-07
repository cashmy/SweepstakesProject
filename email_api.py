import smtplib
import ssl


class EmailApi:
    def __init__(self):
        # password = input("Type your password and press enter: ")
        self.password = "devcmc60$"
        self.login_user = "developercmc60@gmail.com"
        self.sender_email = "developercmc60@gmail.com"
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # For starttls

    receiver_email = "cmyers880@gmail.com"

    def connect_and_send(self, email_list, winner_name):
        message_text = ('\\n'
                        'Subject: Hi there\n'
                        '\n'
                        'This message is to inform you about the sweepstakes winner.\n'
                        f'It is {winner_name}!')
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)

            # TODO: Send email here
            for receiver in email_list:
                server.sendmail(self.sender_email, receiver, message_text)

        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()

