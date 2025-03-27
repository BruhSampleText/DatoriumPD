from server import admin, database, application

import re;
import flask;

def parse_query( query ):
	return re.findall( r'\w+', query.lower() )


@application.route( "/get/tags" )
def route_get_tags():
	return flask.jsonify( database.get_tags_for_client() )

@application.route( "/post/search", methods=["GET", "POST"] )
def	route_post_search():
	query = flask.request.args.get( "query", "" )
	
	parsed = parse_query( query )

	return flask.render_template( 
		"post_search.html", 
		results = database.get_posts_with_tags( parsed ),
		search_term = " ".join( str(x) for x in parsed ) 
	)