from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Comment import CommentResource
from resources.Category import CategoryResource
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
