import random;
import math;

from flask_peewee.db import Database
from peewee import TextField, CharField, DateTimeField, ForeignKeyField, fn

from server import application

db = Database( application )


### Database thingies

class PostDB( db.Model ):
	title = TextField()
	date = DateTimeField()

class TagDB( db.Model ):
	tag = CharField( unique=True )
	description = TextField()

class PostTagDB( db.Model ):
	post = ForeignKeyField( PostDB, backref = "tags" )
	tag = ForeignKeyField( TagDB, backref = "posts" )

class PostImageDB( db.Model ):
	post = ForeignKeyField( PostDB, backref="image" )
	image = TextField( null=True )


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

def get_posts_with_tags( tags ):

	tags = TagDB.select().where( TagDB.tag.in_( tags ) )
	tag_ids = [tag.id for tag in tags]

	tag_count = len(tag_ids)

	result = ( PostDB.select()
		.join( PostTagDB )
		.where( PostTagDB.tag.in_(tag_ids) )
		.group_by( PostDB )
		.having( fn.COUNT(PostTagDB.tag) == tag_count )
	)

	return result

def get_tags_for_client():
	return [ tag.tag for tag in TagDB.select() ]

def get_images_for_post( post_id ):
	all_related_images = PostImageDB.select().where( PostImageDB.post.id == post_id )
	return [ img.image for img in all_related_images ]

def get_tag( name ):
	return (
		TagDB.select().where( TagDB.tag == name.lower() )
	)