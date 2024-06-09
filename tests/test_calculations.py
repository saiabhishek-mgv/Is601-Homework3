'''My Calculator Test'''
from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract
# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
@pytest.fixture
def calculation_setup():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(calculation_setup):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(calculation_setup):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(calculation_setup):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(calculation_setup):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(calculation_setup):
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
