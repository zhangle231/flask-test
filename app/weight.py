from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)

import logging
from app import my_db

bp = Blueprint('weight', __name__, url_prefix='/weight')

@bp.route('/')
def index():
	return render_template('weight/index.html')	


@bp.route('/add', methods=('GET', 'POST'))
def add():
	if request.method == "POST":
		return redirect(url_for('weight.index'))
	return render_template('weight/add.html')

class Weight(my_db.Model):
	id = my_db.Column(my_db.Integer, primary_key=True)
	date = my_db.Column(my_db.Date())
	weight = my_db.Column(my_db.Float())

	def __repr__(self):
		return 'Weight date:%r, weight:%r' % (self.date, self.weight)

def save_weight(weight):
	my_db.session.add(weight)
	my_db.session.commit()
	pass

