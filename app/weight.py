from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)

import datetime
import logging
from app import my_db

bp = Blueprint('weight', __name__, url_prefix='/weight')

@bp.route('/')
def index():
	return render_template('weight/index.html')	


@bp.route('/add', methods=('GET', 'POST'))
def add():
	if request.method == "POST":
		logging.error('------------' + str(request.form['date']))
		logging.error('------------' + str(request.form['weight']))
		weight = Weight()
		
		date = datetime.datetime.strptime(request.form['date'],"%Y-%m-%d")
		weight.date = date
		weight.weight = request.form['weight']
		logging.error('------------' + str(weight))
		save_weight(weight)
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

