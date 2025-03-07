
import flask;

application = flask.Flask( __name__ )

SECRET_KEY = "Polim patīk mazas meitenītes"
DATABASE = {
	"name": "bogWater.db",
	"engine": "peewee.SqliteDatabase"
}

application = flask.Flask(
	__name__,
	template_folder = "../templates",
	static_folder = "../static"
	) 
application.config.from_object(__name__)

from server import database;
from server import views;
from server import admin;