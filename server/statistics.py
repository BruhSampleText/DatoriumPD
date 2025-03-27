from server import admin, database, application;

import matplotlib.pyplot as plot;
import pandas as panda;
import flask;

def generate_histogram_data():
	data_frame = panda.DataFrame( 
		list(
			database.PostDB.select()
			.dicts()
		)
	)

	data_frame[ "weekday" ] = data_frame[ "date" ].dt.day_name()

	plot.hist( data_frame[ "weekday" ], bins = 7 )
	#plot.xlabel()
	#plot.ylabel()
	#plot.title()
	plot.savefig( "server\static\images\dynamic\hist.png", dpi=300 )
	plot.close()



@application.route( "/statistics" )
def	route_statistics():
	generate_histogram_data()
	return flask.render_template( "statistics.html" )
