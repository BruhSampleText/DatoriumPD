
import flask;

application = flask.Flask( __name__ )

SECRET_KEY = "BingBongSkibidit toiket 69420 amognusf sdnsjfnsekfngedkfnsfndjehnfsjfndjf sdjfmjf"
DATABASE = {
	"name": "bogWater.db",
	"engine": "peewee.SqliteDatabase"
}

application = flask.Flask(
	__name__,
	#template_folder = "../templates",
	#static_folder = "../static"
	) 
application.config.from_object(__name__)

from server import database;
from server import views;
from server import search;
from server import admin;
from server import statistics;