# tests/test_home.py
from pages.home_page import HomePage


def test_home_page_title(logged_in_browser):
    home_page = HomePage(logged_in_browser)
    home_page.open()

    # Print the actual title to verify what it returns
    print(f"Actual Page Title: {home_page.get_title()}")

    # Assert the title matches your expectations
    assert "Dashboard" in home_page.get_title()
