from server import admin, database, application

import flask;

@application.route( "/" )
def route_main():
	query = database.get_most_recent()

	for thinfy in query:
		print( thinfy.title + " @ " + str( thinfy.date.year )  )

	return flask.render_template( "main.html", posts = query )

@application.route( "/get/page/<int:page>" )
def	route_get_page( page ):
	return flask.render_template( "main.html", posts = database.get_page( page ) )


## Retarded crap

@application.route( "/crateadmin" )
def	route_dev_create_admin():
	new_user = admin.auth.User( username="admin", email="", admin=True, active=True )
	new_user.set_password( "admin" )
	new_user.save()

	return "Admin acount created!"

@application.route( "/drop_database" )
def route_dev_drop_db():
	database.PostDB.drop_table()
	database.TagDB.drop_table()