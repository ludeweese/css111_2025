# Team Activity week 05

"""Functions to manipulate full names in "Family; Given" format."""

def make_full_name(given_name, family_name):
    """Combine given name and family name into 'Family; Given' format."""
    # Add a space after the semicolon
    return f"{family_name}; {given_name}"

def extract_family_name(full_name):
    """Extract the family name from a full name in 'Family; Given' format."""
    # Split the string at the semicolon and strip whitespace
    return full_name.split(";")[0].strip()

def extract_given_name(full_name):
    """Extract the given name from a full name in 'Family; Given' format."""
    # Split the string at the semicolon and strip whitespace
    parts = full_name.split(";")
    if len(parts) > 1:
        return parts[1].strip()
    return ""
