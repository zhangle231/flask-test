from flask import (Blueprint)

bp = Blueprint('photo', __name__, url_prefix='/photo')

@bp.route('/')
def index():
    return 'photo'

@bp.route('/list')
def list():
    return 'photo'
