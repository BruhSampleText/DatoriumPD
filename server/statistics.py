from server import admin, database, application;

import matplotlib.pyplot as plot;
import pandas as panda;
import flask;

def generate_histogram():
	data_frame = panda.DataFrame( 
		list(
			database.PostDB.select()
			.dicts()
		)
	)

	print( data_frame )
	data_frame[ "date" ] = panda.to_datetime( data_frame[ "date" ] )
	data_frame[ "weekday" ] = data_frame[ "date" ].dt.day_name(  )

	plot.hist( data_frame[ "weekday" ], bins = 7 )
	plot.xlabel( "Days of the week" )
	plot.ylabel( "Entries" )
	plot.title( "Lost entry distributin per day" )
	plot.savefig( "server/static/images/dynamic/hist.svg" )
	plot.close()

def generate_most_used_tag_per_day_heatmap():
	data_frame = panda.DataFrame(
		list(
			database.PostTagDB.select( database.PostTagDB.tag )
			.dicts()
		)
	)

	print( data_frame )

	data_frame_count = data_frame[ "tag" ].value_counts().reset_index()
	data_frame_count.columns = [ "tag", "count" ]



	print( data_frame_count )


@application.route( "/statistics" )
def	route_statistics():
	generate_histogram()
	#generate_most_used_tag_per_day_heatmap()
	#generate_histogram_entries()
	return flask.render_template( "statistics.html" )
