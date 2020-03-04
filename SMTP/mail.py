class mail:
    def __init__(self, server, port, sender, password):
        self.server = server
        self.port = port
        self.sender = sender
        self.password = password
        self.attachment = True

    def send(self, sender, receiver, attachment):
        if attachment:
            from email.mime.base import MIMEBase
            from email import encoders
            from email.mime.multipart import MIMEMultipart

            msg = MIMEMultipart('mixed')
            files = ['test.md', 'test2.md']
            for file in files:

                with open(file, 'rb') as f:
                    file_data = MIMEBase("application", "octect-stream")
                    file_data.set_payload(f.read())
                    encoders.encode_base64(file_data)
                    file_data.add_header("Content-Disposition", "attachment", file_name=file)
                    msg.attach(file_data)
            msg

            for i in receiver:
                msg['To'] = i

        else:
            from email.mime.text import MIMEText
            msg = MIMEText('test message')
            for i in receiver:
                msg['To'] = i
        msg['From'] = sender
        msg['Subject'] = 'subject'

        return msg

    def test(self):
        receiver = ['', '']  # 입력필요

        s = mail(server, port, sender, password)

        s = smtplib.SMTP(server, port)
        s.starttls()
        s.login(sender, password)
        msg = self.send(sender, receiver, attachment=True)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()


if __name__ == '__main__':
    import smtplib

    server = 'smtp.gmail.com'
    port = 587
    sender = ''  # 입력필요
    password = ''  # 입력필요

    smtp = mail(server, port, sender, password)
    smtp.test()
