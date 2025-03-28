from server import admin, database, application

import flask;

@application.route( "/" )
def route_main():
	query = database.get_most_recent()
	return flask.render_template( "index.html", posts = query )

@application.route( "/get/page/<int:page>" )
def	route_get_page( page ):
	query = database.get_page( page )

	for thinfy in query:
		print( thinfy.title + " @ " + str( thinfy.date.year ) + " | id: " + str(thinfy.id) )
	return flask.render_template( "main.html", posts = query )

@application.route( "/post/view/<int:id>" )
def	route_post_view( id ):
	return flask.render_template( "post_view.html", data = database.get_page( id ) )


# They/them complex thingies

from server import search;
from server import create;
from server import statistics;