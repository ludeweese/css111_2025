# test_full_oaks_conference_talks.py
from full_oaks_conference_talks import (
    load_talks_from_csv,
    get_all_talks,
    get_talks_by_year,
    get_talks_by_keyword,
    sort_talks,
    save_talks_to_csv
)
import pytest
import os

# -----------------------------
# Test load_talks_from_csv
# -----------------------------
def test_load_talks_from_csv():
    """Verify that talks are loaded from CSV correctly."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    talks = get_all_talks()
    assert isinstance(talks, list), "get_all_talks should return a list"
    assert len(talks) > 0, "The list of talks should not be empty"
    first_talk = talks[0]
    for key in ["Title", "Date", "Session", "URL"]:
        assert key in first_talk, f"Missing key '{key}' in talk"

# -----------------------------
# Test get_talks_by_year
# -----------------------------
def test_get_talks_by_year():
    """Verify that get_talks_by_year returns correct talks for a year."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    year = 1984
    talks_1984 = get_talks_by_year(year)
    assert isinstance(talks_1984, list), "get_talks_by_year should return a list"
    assert len(talks_1984) > 0, "There should be at least one talk in 1984"
    for talk in talks_1984:
        assert str(year) in talk["Date"], f"Talk {talk['Title']} is not from {year}"

# -----------------------------
# Test get_talks_by_keyword
# -----------------------------
def test_get_talks_by_keyword():
    """Verify that get_talks_by_keyword returns talks containing the keyword."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    keyword = "Faith"
    talks_with_keyword = get_talks_by_keyword(keyword)
    assert isinstance(talks_with_keyword, list), "get_talks_by_keyword should return a list"
    assert len(talks_with_keyword) > 0, "There should be at least one talk with keyword"
    for talk in talks_with_keyword:
        assert keyword.lower() in talk["Title"].lower(), f"Talk {talk['Title']} does not contain '{keyword}'"

# -----------------------------
# Test sort_talks
# -----------------------------
def test_sort_talks():
    """Verify that sort_talks returns talks sorted by title."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    sorted_talks = sort_talks()
    titles = [talk["Title"] for talk in sorted_talks]
    assert titles == sorted(titles), "Talks are not sorted alphabetically by title"

# -----------------------------
# Test save_talks_to_csv
# -----------------------------
def test_save_talks_to_csv(tmp_path):
    """Verify that save_talks_to_csv correctly writes a CSV file."""
    load_talks_from_csv("president_Oaks_Talks.csv")
    talks = get_all_talks()
    test_file = tmp_path / "test_output.csv"
    save_talks_to_csv(talks, str(test_file))
    # Verify the file exists
    assert os.path.exists(test_file), "CSV file was not created"
    # Verify file is not empty
    with open(test_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) > 1, "CSV file is empty"

# -----------------------------
# Run pytest if file executed directly
# -----------------------------
pytest.main(["-v", "--tb=line", "-rN", __file__])
