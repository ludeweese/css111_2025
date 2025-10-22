# address.py
"""Functions to extract parts of an address in 'number street, city, state zipcode' format."""

def extract_city(address):
    """Extract the city from an address."""
    try:
        parts = address.split(",")
        if len(parts) < 2:
            return ""
        return parts[1].strip()
    except IndexError:
        return ""

def extract_state(address):
    """Extract the state from an address."""
    try:
        parts = address.split(",")
        if len(parts) < 3:
            return ""
        state_zip = parts[2].strip().split()
        if len(state_zip) < 2:
            return ""
        return state_zip[0]  # state abbreviation
    except IndexError:
        return ""

def extract_zipcode(address):
    """Extract the zipcode from an address."""
    try:
        parts = address.split(",")
        if len(parts) < 3:
            return ""
        state_zip = parts[2].strip().split()
        if len(state_zip) < 2:
            return ""
        return state_zip[1]  # zipcode
    except IndexError:
        return ""
