import pytest
import logging
import datetime

from app.weight import (
    save_weight,Weight
)

def test_save_weight(app):
    with app.app_context():
        weight = Weight()
        date = datetime.date(2020,5,10)
        weight.date = date
        weight.weight = 200
        save_weight(weight)
    pass
