import smtplib as smtp


def send_email(msg, recipients):
    try:
        connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        email_addr = 'sender_email_adress'
        email_passwd = 'sender_app_password'
        connection.login(email_addr, email_passwd)
        connection.sendmail(from_addr=email_addr, to_addrs=recipients, msg=msg)
        connection.close()
    except:
        print("Error")


recipients = input("Email: ")
msg = input("Msg: ")
if __name__ == '__main__':
    send_email(msg, recipients)
