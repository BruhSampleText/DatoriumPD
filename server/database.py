import random;
import math;

from flask_peewee.db import Database
from peewee import TextField, IntegerField, FloatField

from server import application

db = Database( application )


### Database thingies

class PostDB( db.Model ):
	title = TextField()

class TagDB( db.Model ):
	tag = TextField()
	description = TextField()


### CONTENT PROVIDING

PAGE_SIZE = 3
def get_page( page_index ):
	return PostDB.select()


def get_most_recent():
	return get_page( math.floor( random.random() * 3 ) )