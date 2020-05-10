import pytest
import logging

from app.weight import (
    save_weight,Weight
)

def test_save_weight(app):
    with app.app_context():
        weight = Weight()
        weight.weight = 200
        save_weight(weight)
    pass
