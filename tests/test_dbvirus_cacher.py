"""
Unit tests for cacher structures
"""
from datetime import datetime
from pytz import utc

from dbvirus_cacher import documents


def test_search_result_created_at():
    """
    tests if a new search result is created with the correct
    created_at value
    """

    result = documents.SearchResult()

    # This test should probably mock datetime.now
    now = datetime.now(utc)
    delta = now - result.created_at

    assert delta.total_seconds() < 200
