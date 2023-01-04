import boto3
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()

eur_usd = round(yf.Ticker('EURUSD=X').history(period='1d')['Close'][0],2)
gbp_usd = round(yf.Ticker('GBPUSD=X').history(period='1d')['Close'][0],2)
eur_gbp = round(yf.Ticker('EURGBP=X').history(period='1d')['Close'][0],2)


ses = boto3.client("ses", region_name="eu-west-2", aws_access_key_id="need_ley_here",
                                aws_secret_access_key="Need access key here")

sent_from = "your_domain@agnon.com"
receiver_email = "receiver_email"
subject = 'Daily FX rates'
body = f'EUR to USD {eur_usd}, GBP to USD {gbp_usd}, EUR to GBP {eur_gbp}'
CHARSET = "UTF-8"

html = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)


response = ses.send_email(
            Destination={
                "ToAddresses": [
                    receiver_email,
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": CHARSET,
                        "Data": html,
                    }
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": "Verify Email AthenaNet",
                },
            },
            Source=sent_from,
        )


