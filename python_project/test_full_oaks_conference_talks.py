# test_full_oaks_conference_talks.py
from full_oaks_conference_talks import load_talks_from_csv, get_all_talks, get_talks_by_year
import pytest

# Test load_talks_from_csv
def test_load_talks_from_csv():
    """Verify that talks are loaded from CSV correctly."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    talks = get_all_talks()
    assert isinstance(talks, list), "get_all_talks should return a list"
    assert len(talks) > 0, "The list of talks should not be empty"
    # Check that the first talk has the correct keys
    first_talk = talks[0]
    for key in ["Title", "Date", "Session", "URL"]:
        assert key in first_talk, f"Missing key '{key}' in talk"

# Test get_talks_by_year
def test_get_talks_by_year():
    """Verify that get_talks_by_year returns correct talks for a year."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    year = 1984
    talks_1984 = get_talks_by_year(year)
    assert isinstance(talks_1984, list), "get_talks_by_year should return a list"
    assert len(talks_1984) > 0, "There should be at least one talk in 1984"
    for talk in talks_1984:
        assert str(year) in talk["Date"], f"Talk {talk['Title']} is not from {year}"

# Run pytest if file executed directly
pytest.main(["-v", "--tb=line", "-rN", __file__])
