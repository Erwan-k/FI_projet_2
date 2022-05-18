from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes.exemple_route import exemple_route,exemple_route_all

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(exemple_route,"/exemple_route") 
api.add_resource(exemple_route_all,"/exemple_route_all") 

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
