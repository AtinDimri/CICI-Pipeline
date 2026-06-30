import pytest
from app import calculate_total

def test_normal_capse(): 
    assert calculate_total(100, 0.10) == 110

def test_zero_price(): 
    assert calculate_total(0, 0.10) == 0

def test_zero_tax(): 
    assert calculate_total(100, 0) == 100

def test_negative_price():
    with pytest.raises(ValueError): 
        calculate_total(-10, 0.10)

def test_negative_tax():
    with pytest.raises(ValueError): 
        calculate_total(100, -0.05)

def test_high_tax(): 
    assert calculate_total(100, 1.0) == 200