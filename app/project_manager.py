from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

import os

from app.db import get_db

bp = Blueprint('project', __name__, url_prefix='/project')

@bp.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return current_app.config['UPLOAD_FOLDER']
        return render_template('blog/create.html')
    return render_template('project/upload.html')
