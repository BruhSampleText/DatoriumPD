import random;
import math;

from flask_peewee.db import Database
from peewee import TextField, IntegerField, FloatField

from server import application

db = Database( application )

BOGUS_DATA = [
	{ "name": "Kurpe" },
	{ "name": "Zābaks" },
	{ "name": "Telefons" },
	{ "name": "Radio" },
	{ "name": "Amartizātors" },
	{ "name": "Brokolis" },
]

PAGE_SIZE = 3
def get_page( page_index ):
	return BOGUS_DATA[ page_index * PAGE_SIZE : page_index * PAGE_SIZE + PAGE_SIZE ]


### Database thingies

class PostDB( db.Model ):
	title = TextField()

class TagDB( db.Model ):
	tag = TextField()
	description = TextField()

### CONTENT PROVIDING

def get_most_recent():
	return get_page( math.floor( random.random() * 3 ) )