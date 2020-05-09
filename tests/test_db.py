import sqlite3
import logging
import pytest

from app.db import get_db

logging.basicConfig(level=logging.DEBUG)

def test_get_close_db(app):
  with app.app_context():
    db = get_db()
    assert db is get_db()

  with pytest.raises(sqlite3.ProgrammingError) as e:
    db.execute('SELECT 1')
    assert 'closed' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False
    def fake_init_db():
        logging.info('fake_init_db is called')
        Recorder.called = True
    monkeypatch.setattr('app.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    logging.info(result.output)
    assert 'Initialized' in result.output
    assert Recorder.called
