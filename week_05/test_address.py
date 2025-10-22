# test_address.py
from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Test extract_city with various addresses."""
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("123 Main St, New York, NY 10001") == "New York"
    assert extract_city("456 Elm St, Los Angeles, CA 90001") == "Los Angeles"
    # Edge case: missing city
    assert extract_city("123 Main St,, NY 10001") == ""

def test_extract_state():
    """Test extract_state with various addresses."""
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("123 Main St, New York, NY 10001") == "NY"
    assert extract_state("456 Elm St, Los Angeles, CA 90001") == "CA"
    # Edge case: missing state
    assert extract_state("123 Main St, New York, 10001") == ""

def test_extract_zipcode():
    """Test extract_zipcode with various addresses."""
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("123 Main St, New York, NY 10001") == "10001"
    assert extract_zipcode("456 Elm St, Los Angeles, CA 90001") == "90001"
    # Edge case: missing zipcode
    assert extract_zipcode("123 Main St, New York, NY") == ""

# Call pytest
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
