#!/usr/bin/env python
from bs4 import BeautifulSoup
import datetime
import requests
import boto3

today = datetime.date.today()
idx = (today.weekday() + 1) % 7
last_sunday = (today - datetime.timedelta(idx))

response = requests.get('http://www.ihefc.org/home/sermons.aspx')

soup = BeautifulSoup(response.text, "html.parser")

recent_link = []
for link in soup.findAll('a', attrs={'class': 'audioLink'}):
    sermon_link = link['href']

    if str(last_sunday) in sermon_link:
        recent_link.append(sermon_link)

if not recent_link:
    print("Audio URL not present")

test_link = requests.head(recent_link[0])
if test_link.status_code != 200:
    ses_response = ses.send_email(
        Source = email_from,
    )
