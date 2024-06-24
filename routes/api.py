from flask import Blueprint, jsonify, make_response, request
api = Blueprint('api', __name__)

@api.route('/')

def home():

    return make_response(
    jsonify({"msg":"OK", "code": 200}),
    200
    )

