import pytest
from bank_app import transfer, calculate_interest

def test_transfer_success():
    b_from, b_to = transfer(5000, 2000, 1000)
    assert b_from == 4000
    assert b_to == 3000

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(500, 1000, 800)

def test_transfer_then_interest():
    b_from, b_to = transfer(10000, 3000, 2000)
    updated_balance = calculate_interest(b_to, 5, 1)
    assert updated_balance == pytest.approx(5250)
