from flask_restful import Resource, reqparse

from utils import getMysqlConnection,ajouter_user

exemple_route_get_args = reqparse.RequestParser()
exemple_route_get_args.add_argument("user",type=str,required=True)
exemple_route_post_args = reqparse.RequestParser()
exemple_route_post_args.add_argument("user",type=str,required=True)
exemple_route_post_args.add_argument("password",type=str,required=True)
exemple_route_put_args = reqparse.RequestParser()
exemple_route_put_args.add_argument("user",type=str,required=True)
exemple_route_put_args.add_argument("password",type=str,required=True)
exemple_route_delete_args = reqparse.RequestParser()
exemple_route_delete_args.add_argument("user",type=str,required=True)

class exemple_route(Resource):
	def get(self): #récupérer le mot de passe d'un utilisateur
		body = exemple_route_get_args.parse_args()
		[user] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'utilisateur existe
		mycursor.execute("SELECT count(*) FROM Utilisateur WHERE user = \""+user+"\"")
		if not mycursor.fetchone()[0]:
			mycursor.close()
			mydb.close()
			return {"retour":"L'utilisateur n'existe pas."}

		#Je récupère son mot de passe
		mycursor.execute("SELECT mdp FROM Utilisateur WHERE user = \""+user+"\"")
		mdp = mycursor.fetchone()[0]

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeur":mdp}

	def post(self): #ajouter un utilisateur
		body = exemple_route_post_args.parse_args()
		[user,password] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'utilisateur existe
		mycursor.execute("SELECT count(*) FROM Utilisateur WHERE user = \""+user+"\"")
		if mycursor.fetchone()[0]:
			mycursor.close()
			mydb.close()
			return {"retour":"L'utilisateur existe déjà."}

		#J'ajoute l'utilisateur
		ajouter_user(user,password,mycursor,mydb)

		mycursor.close()
		mydb.close()
		
		return {"retour":"ok"}

	def put(self): #modifier le mot de passe d'un utilisateur
		body = exemple_route_put_args.parse_args()
		[user,password] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'utilisateur existe
		mycursor.execute("SELECT count(*) FROM Utilisateur WHERE user = \""+user+"\"")
		if not mycursor.fetchone()[0]:
			mycursor.close()
			mydb.close()
			return {"retour":"L'utilisateur n'existe pas."}

		#Je modifie le mot de passe de l'utilisateur
		mycursor.execute("UPDATE Utilisateur SET  mdp = \""+password+"\" WHERE user = \""+user+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()
		
		return {"retour":"ok"}

	def delete(self): #supprimer_un_match
		body = exemple_route_delete_args.parse_args()
		[user] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'utilisateur existe
		mycursor.execute("SELECT count(*) FROM Utilisateur WHERE user = \""+user+"\"")
		if not mycursor.fetchone()[0]:
			mycursor.close()
			mydb.close()
			return {"retour":"ok","note":"L'utilisateur n'existait pas."}

		#Je supprime l'utilisateur
		mycursor.execute("DELETE FROM Utilisateur WHERE user = \""+user+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()
		
		return {"retour":"ok"}

class exemple_route_all(Resource):
	def get(self):
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		mycursor.execute("SELECT user,mdp FROM Utilisateur")
		s = [{"user":i[0],"mdp":i[1]} for i in mycursor.fetchall()]

		mycursor.close()
		mydb.close()
		
		return {"retour":"ok","valeur":s}


