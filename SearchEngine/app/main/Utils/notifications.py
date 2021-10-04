import smtplib
# login notification sent to mail
def login_notification(receiver):
    try:
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('gmnithinsai2599@gmail.com', 'hyyj douo hcyj wlrd')
            subject = 'Welcome to Search Engine'
            body = 'Hey user!\n\nYou have been succesfully logged into the search engine powered by skill assure\n\nStart surfing in our search engine and Have a good time \n\nThankyou.'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail('gmnithinsai2599@gmail.com',receiver,msg)
    except:
        print("Email was not sent")
            

    