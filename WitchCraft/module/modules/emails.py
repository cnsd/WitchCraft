#emails.py
import requests
from bs4 import BeautifulSoup

def get_mailtester_data(email_address):
	response_text = requests.post('http://mailtester.com/testmail.php', data={'lang':'en', 'email':email_address}).text
	if 'Invalid' in response_text:
		return 'The domain is invalid or no mail server was found for it.'

	soup_text = BeautifulSoup(response_text)
	soup_trs = soup_text.findAll('table')[1].findAll('tr')
	soup_tds = soup_trs[len(soup_trs) - 1].findAll('td')
	mailtester_result = str(soup_tds[len(soup_tds) - 1])

	return mailtester_result[21:].replace('</td>', '')[1:]