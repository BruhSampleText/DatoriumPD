import flask;

from server import application, database;

@application.route( "/" )
def route_main():
	return flask.render_template( "main.html", posts = database.get_page( 1 ) )

@application.route( "/get/page/<int:page>" )
def	route_get_page( page ):
	return flask.render_template( "main.html", posts = database.get_page( page ) )
