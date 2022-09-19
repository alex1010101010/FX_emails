import smtplib
import yfinance as yf

gmail_user = 'clickforthedeal@gmail.com'
gmail_password = 'hqbvtqpgvsdfuztc'


eur_usd = round(yf.Ticker('EURUSD=X').history(period='1d')['Close'][0],2)
gbp_usd = round(yf.Ticker('GBPUSD=X').history(period='1d')['Close'][0],2)
eur_gbp = round(yf.Ticker('EURGBP=X').history(period='1d')['Close'][0],2)

sent_from = gmail_user
to = ['alexspellanzon@gmail.com']
subject = 'Daily FX rates'
body = f'EUR to USD {eur_usd}, GBP to USD {gbp_usd}, EUR to GBP {eur_gbp}'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)