from bs4 import BeautifulSoup
import requests

response = requests.get('http://www.ihefc.org/home/sermons.aspx')

soup = BeautifulSoup(response.txt)
