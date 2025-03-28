from flask_peewee.auth import Auth
from flask_peewee.admin import Admin, ModelAdmin

from server import application
from server import database

auth = Auth( application, database.db )
admin = Admin( application, auth )


class AdminUser( ModelAdmin ):
	columns: ( "name" )


admin.register( database.TagDB , AdminUser )
admin.register( database.PostDB, AdminUser )
admin.register( database.PostTagDB, AdminUser )
admin.register( database.PostImageDB, AdminUser )

admin.setup()
