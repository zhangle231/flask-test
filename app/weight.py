from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)


bp = Blueprint('weight', __name__, url_prefix='/weight')

@bp.route('/')
def index():
	return render_template('weight/index.html')	
