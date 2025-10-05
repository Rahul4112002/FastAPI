import pytest
from app.logic import is_eligible_for_loan


def test_eligible_user():
    assert is_eligible_for_loan(60000, 25, 'employed') == True


def test_underage_user():
    assert is_eligible_for_loan(60000, 19, 'employed') == False


def test_low_income():
    assert is_eligible_for_loan(30000, 25, 'employed') == False


def test_unemployed_user():
    assert is_eligible_for_loan(60000, 25, 'unemployed') == False


def test_boundary_case():
    assert is_eligible_for_loan(50000, 21, 'employed') == True