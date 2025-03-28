from server import admin, database, application;

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import pandas as panda;
import flask;
import io;

@application.route( "/histogram" )
def serve_histogram():
	data_frame = panda.DataFrame( 
		list(
			database.PostDB.select()
			.dicts()
		)
	)

	data_frame[ "date" ] = panda.to_datetime( data_frame[ "date" ] )
	data_frame[ "weekday" ] = data_frame[ "date" ].dt.day_name(  )

	figure = Figure()
	axis = figure.subplots()

	axis.hist( data_frame[ "weekday" ], bins = 7 )
	axis.set_title( "Lost entry distribution per day" )
	axis.set_xlabel( "Days of the week" )
	axis.set_ylabel( "Entries" )

	img = io.BytesIO()
	figure.savefig( img, format="png" )
	img.seek( 0 )

	return flask.Response(img.getvalue(), mimetype="image/png")


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
	return flask.render_template( "statistics.html" )
