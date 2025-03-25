from server import admin, database, application

import flask;


def validate_search_query( query ):
	tags = query.strip( ",.][)(-+*/" ).lower().split( " " )
	valid_tags = []
	for a in tags:
		print( a )
		tag = database.get_tag( a )
		if tag.exists():
			print( a + " exists!" )
			valid_tags.append( tag[0].id )

	return valid_tags

@application.route( "/post/search", methods=['GET', 'POST'] )
def	route_post_search():
	
	search_term = ""
	result = []
	if flask.request.method == "GET":
		query = flask.request.args.get( "query", "" )
		print( "Debug: " + query )
		search_term = query
		tags = validate_search_query( query )
		result = database.find_all_with_tag_ids( tags )
		result = database.PostDB.select().where( database.PostDB.id.in_( result ) )
	


	return flask.render_template( "post_search.html", results = result, search_term = search_term )
