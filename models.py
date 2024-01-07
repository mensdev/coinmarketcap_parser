from peewee import *
from config import db

class Coins(Model):
	symb = CharField(10)
	name = CharField(100)
	link = CharField(unique = True)

	class Meta:
		database = db