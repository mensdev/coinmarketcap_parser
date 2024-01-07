from peewee import *

class Config():
	DEBUG = True

db = SqliteDatabase('db.sqlite',{
	'journal_mode': 'wal',
	'cache_size': -1024 * 32
	})