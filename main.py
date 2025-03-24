from server import application, database, admin;


if __name__ == "__main__":
	admin.auth.User.create_table(fail_silently=True)
	database.TagDB.create_table(fail_silently=True)
	database.PostDB.create_table(fail_silently=True)
	database.PostTagDB.create_table(fail_silently=True)
	
	application.run( debug = True )