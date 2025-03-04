import random;
import math;

from flask_peewee.db import Database
from peewee import TextField, IntegerField, FloatField, DateTimeField

from server import application

db = Database( application )


### Database thingies

class PostDB( db.Model ):
	title = TextField()
	date = DateTimeField()

class TagDB( db.Model ):
	tag = TextField()
	description = TextField()



### CONTENT PROVIDING

#http://docs.peewee-orm.com/en/latest/peewee/api.html#Model.select
#http://docs.peewee-orm.com/en/latest/peewee/api.html#Query.where

PAGE_SIZE = 5
def get_page( page_index ):
	return (
		PostDB.select()
		.where( PostDB.id >= (page_index * PAGE_SIZE) )
		.where( PostDB.id < (page_index * PAGE_SIZE + PAGE_SIZE ) )
		.order_by( PostDB.date.desc() )
		)

def get_most_recent( count = PAGE_SIZE ):
	return PostDB.select().limit( count ).order_by( PostDB.date.desc() )