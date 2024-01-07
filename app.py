from flask import Flask
from peewee import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


