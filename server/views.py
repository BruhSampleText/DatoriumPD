from server import admin, database, application

import flask;

@application.route( "/" )
def route_main():
	return flask.render_template( "main.html", posts = database.get_most_recent() )

@application.route( "/get/page/<int:page>" )
def	route_get_page( page ):
	return flask.render_template( "main.html", posts = database.get_page( page ) )

@application.route( "/crateadmin" )
def	route_dev_create_admin():
	new_user = admin.auth.User( username="admin", email="", admin=True, active=True )
	new_user.set_password( "admin" )
	new_user.save()

	return "Admin acount created!"