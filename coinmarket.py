import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
from multiprocessing import Pool
from peewee import *
from config import db
from models import Coins as Coin

def count_time(func):
	def wrapper(*args):
		start = datetime.now()
		res = func(*args)
		print(func.__name__+ ' > ' + str(datetime.now() - start))
		return res
	return wrapper

def write_csv(data):
	order = ['symb','name', 'link']
	with open('coins.csv', 'r+') as f:
		reader = csv.DictReader(f, fieldnames = order)
		writer = csv.DictWriter(f, fieldnames = order)
		
		if data not in reader:
			print(data)
			writer.writerow(data)

'''db = SqliteDatabase('coins.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})'''
#db = PostgresqlDatabase('test', user='admin', password='1', host='localhost')

@count_time
def main():
	db.connect()
	db.create_tables([Coin])

	'''try:
		os.remove('coins.csv')
	except:
		pass'''
	html = requests.get('https://coinmarketcap.com/all/views/all/').text
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find('table', id='currencies-all').find('tbody').find_all('tr')

	count = 0
	#data = []
	for tr in trs:
		tds = tr.find_all('td')
		name = tds[1].get('data-sort')
		symb = tds[1].find('a').text
		link = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
		try:
			with db.atomic():
				Coin.get_or_create(symb = symb, name = name, link = link)
		except:
			print('err')
			#pass

		#mysql 7.49 s
		#postgresql 6.9 s
		#sqlite 5.87 s
		#pool with list 7.59
		#pool with tuple 7.88 s
		#for 14.98 s
		'''
		write_csv({'symb':symb, 'name': name, 'link': link})
		'''

		count += 1

		'''data.append({'symb':symb, 'name': name, 'link': link})

	with Pool(10) as p:
		p.map(write_csv, data)'''

	print('Total: ' + str(count))


if __name__ == '__main__':
	main()