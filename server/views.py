from server import admin, database, application

import flask;

@application.route( "/" )
def route_main():
	query = database.get_most_recent()
	return flask.render_template( "index.html", posts = query )

@application.route( "/get/page/<int:page>" )
def	route_get_page( page ):
	query = database.get_page( page )
	return flask.render_template( "main.html", posts = query )


@application.route( "/post/create" )
def	route_post_create():
	return flask.render_template( "post_create.html" )

@application.route( "/post/view<int:id>" )
def	route_post_view():
	bogus_data = {}
	return flask.render_template( "post_view.html", data = bogus_data )

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
	database.PostTagDB.drop_table()