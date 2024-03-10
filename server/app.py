#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Shop

# Views go here!
class Login(Resource):
    def get(self):
        response_dict_list = [user.to_dict() for user in User.query.all()]

        response = make_response(
            response_dict_list,
            200
        )

        return response
    
    def post(self):

        new_user =  User(
            name = request.get_json()
        )

        db.session.add(new_user)
        db.session.commit()

        response = make_response(
            new_user.to_dict(),
            201
        )

        return response

class Shops(Resource):
    def get(self):
        response_dict_list = [shop.to_dict() for shop in Shop.query.all()]

        response = make_response(
            response_dict_list,
            200
        )

        return response
    
    def post(self):
        print('Post request received')

        new_shop =  Shop(
            name = request.get_json()
        )

        return {"message": f"post request handled {new_shop}"}
    

api.add_resource(Login, '/login')
api.add_resource(Shops, '/shops')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

