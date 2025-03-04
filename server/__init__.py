
import flask;

application = flask.Flask( __name__ )

application = flask.Flask(__name__) 
application.config.from_object(__name__)

from server import database;
from server import views;