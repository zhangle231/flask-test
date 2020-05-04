export FLASK_APP=app
export FLASK_ENV=development
nohup python -m flask run --host 0.0.0.0 > log.log 2>&1 &
