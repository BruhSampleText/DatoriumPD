
from flask_peewee.auth import Auth
from flask_peewee.db import Database

from server import application;


BOGUS_DATA = [
	{ "name": "Kurpe" },
	{ "name": "Zābaks" },
	{ "name": "Telefons" },
	{ "name": "Radio" },
	{ "name": "Amartizātors" },
	{ "name": "Brokolis" },
]

PAGE_SIZE = 3
def get_page( page_index ):
	return BOGUS_DATA[ page_index * PAGE_SIZE : page_index * PAGE_SIZE + PAGE_SIZE ]