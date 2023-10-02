from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/all')
def home():
    return {
        "status": "ok",
        "data": 123456
    }