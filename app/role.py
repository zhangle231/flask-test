from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('role', __name__, url_prefix='/role')


@bp.route('/')
def index():
    return render_template('role/index.html')
