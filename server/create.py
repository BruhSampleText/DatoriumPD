from server import admin, database, application

import re;
import flask;
import os;
from datetime import datetime;
from werkzeug.utils import secure_filename

def parse_query( query ):
	return re.findall( r'\w+', query.lower() )

def add_tags_to_post( post_id, tags ):
	for tag in tags:
		db_tag_entry = database.get_tag( tag )
		if not db_tag_entry.exists(): continue

		new_post_tag = database.PostTagDB( 
			tag = db_tag_entry[0].id,
			post = post_id,
		)

		new_post_tag.save()
	
def add_images_to_post( post_id, files ):
	print( files )
	for file in files:
		print( file.filename )

		file_name = secure_filename( file.filename )
		file_path = os.path.abspath( application.root_path + "/static/images/uploaded/" + file_name )

		print( file_name, file_path )

		file.save( file_path )

		new_file = database.PostImageDB( 
			post = post_id,
			image = file_name
		)

		new_file.save()

		print( new_file.id )


@application.route( "/post/create", methods = [ "GET", "POST" ] )
@admin.auth.login_required
def	route_post_create():

	if flask.request.method == "POST":
		title = flask.request.form.get( "post_title" )
		date = flask.request.form.get( "post_date" ); date = datetime.strptime( date, "%Y-%m-%dT%H:%M" )
		tags = flask.request.form.get( "post_tags" )

		new_post = database.PostDB( 
			title = title,
			date = date
		)

		new_post.save()

		tags = parse_query( tags )
		add_tags_to_post( new_post.id, tags )
		add_images_to_post( new_post.id, flask.request.files.getlist( "post_images" ) )

		#return flask.redirect( "/" )

	return flask.render_template( "post_create.html" )
