from unittest.mock import Mock

import pytest

from woven_light.tfl_scraper.scrape import scrape


@pytest.fixture
def mock_tfl_scrape_get(mocker):
    mock = Mock()
    mocker.patch("requests.get", return_value=mock)
    return mock


def test_valid_scrape(mock_tfl_scrape_get):
    mock_tfl_scrape_get.status_code = 200
    mock_tfl_scrape_get.json.return_value = [{"description": "TEST"}]
    returned_description = scrape("test_string")
    assert returned_description == "TEST"


def test_invalid_json_scrape(mock_tfl_scrape_get):
    mock_tfl_scrape_get.status_code = 200
    mock_tfl_scrape_get.json.return_value = [{}]
    returned_description = scrape("test_string")
    assert returned_description is None


def test_400_status_code_invalid_scrape(mock_tfl_scrape_get):
    mock_tfl_scrape_get.status_code = 400
    returned_description = scrape("test_string")
    assert returned_description is None
