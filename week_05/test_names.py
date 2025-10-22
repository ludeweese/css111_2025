# team activity week 05

"""Test functions for names.py using pytest."""

from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """Test make_full_name with various names."""
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Olivier", "Toussaint") == "Toussaint; Olivier"
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"
    # Test empty names
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    """Test extract_family_name with various full names."""
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Smith-Jones; Ava") == "Smith-Jones"
    # Test empty names
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    """Test extract_given_name with various full names."""
    assert extract_given_name("Washington; George") == "George"
    assert extract_given_name("Toussaint; Olivier") == "Olivier"
    assert extract_given_name("Smith-Jones; Ava") == "Ava"
    # Test empty names
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
